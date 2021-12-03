from django.shortcuts import render, redirect
from .forms import ContactForm

from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def predict(request):
    return render(request, 'predict.html', {})

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