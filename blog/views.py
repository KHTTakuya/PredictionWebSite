from datetime import date, datetime
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Prediction, BetToReturn

from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.db.models import Sum, Count
from django.utils.timezone import make_aware


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def predict(request):
    prediction = Prediction.objects.all()
    bet_to_return = BetToReturn.objects.all()

    today = date.today()
    seasons = date(2021, 12, 31)

    total_bet = bet_to_return.aggregate(Sum('bet'))
    total_pay = bet_to_return.aggregate(Sum('payoff'))
    total_count = bet_to_return.aggregate(Count('title'))

    place_list = []

    total_today = 0
    total_season = 0
    today_win = 0
    seasons_win = 0
    today_count = 0
    seasons_count = 0
    win_count = 0

    for pay in bet_to_return:
        # 収支・的中数を確認する。
        if pay.race_time.date() == today:
            today_count += 1
            seasons_count += 1
            total_today += pay.payoff
            if pay.win > 0:
                today_win += 1
        elif pay.race_time.date() < seasons:
            seasons_count += 1
            total_season += pay.payoff
            if pay.win > 0:
                seasons_win += 1
        # 総合単勝的中数確認
        if pay.win > 0:
            win_count += 1

    for pred in prediction:
        if pred.race_time.date() == today:
            place_list.append(pred.place)

    place_list = set(place_list)
    place_list = list(place_list)

    queryset = prediction.filter(race_time__year=today.year,
                                 race_time__month=today.month,
                                 race_time__day=today.day)

    today_place = len(place_list)

    total_season += total_today
    seasons_win += today_win

    if today_place == 1:
        raceset1 = queryset.filter(place=place_list[0])
        get_race1 = raceset1.order_by('race_num')
        get_race2 = None
        get_race3 = None
    elif today_place == 2:
        raceset1 = queryset.filter(place=place_list[0])
        raceset2 = queryset.filter(place=place_list[1])
        get_race1 = raceset1.order_by('race_num')
        get_race2 = raceset2.order_by('race_num')
        get_race3 = None
    elif today_place == 3:
        raceset1 = queryset.filter(place=place_list[0])
        raceset2 = queryset.filter(place=place_list[1])
        raceset3 = queryset.filter(place=place_list[2])
        get_race1 = raceset1.order_by('race_num')
        get_race2 = raceset2.order_by('race_num')
        get_race3 = raceset3.order_by('race_num')
    else:
        get_race1 = None
        get_race2 = None
        get_race3 = None

    context = {
        'today': today,
        'seasons': seasons,
        'prediction': prediction,
        'bet_to_return': bet_to_return,
        'total_today': total_today,
        'total_season': total_season,
        'today_count': today_count,
        'season_count': seasons_count,
        'total_count': total_count,
        'total_bet': total_bet,
        'total_pay': total_pay,
        'win_count': win_count,
        'today_win': today_win,
        'season_win': seasons_win,
        'place_list': place_list,
        'queryset': queryset,
        'get_race1': get_race1,
        'get_race2': get_race2,
        'get_race3': get_race3,
    }

    return render(request, 'predict.html', context)


def detail_predict_post(request, pk):
    post = get_object_or_404(Prediction, pk=pk)
    result_post = BetToReturn.objects.all()

    today = date.today()

    queryset = result_post.filter(race_time__year=today.year,
                                  race_time__month=today.month,
                                  race_time__day=today.day)

    context = {
        'post': post,
        'result_post': result_post,
        'queryset': queryset
    }
    return render(request, 'predict_detail.html', context)


def detail_predict_result(request, pk):
    post = get_object_or_404(BetToReturn, pk=pk)

    context = {
        'post': post
    }
    return render(request, 'predict_detail.html', context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            myself = form.cleaned_data['myself']
            recipients = [settings.EMAIL_HOST_USER]

            if myself:
                recipients.append(email)
            try:
                send_mail(subject=subject, message=message, from_email=email, recipient_list=recipients)
            except BadHeaderError:
                return HttpResponse("無効なヘッダーが見つかりました。")
            return redirect('complete')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def complete(request):
    return render(request, 'complete.html', {})
