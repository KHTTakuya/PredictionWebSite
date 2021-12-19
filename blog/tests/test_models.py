from datetime import datetime, timezone, timedelta
from django.test import TestCase
from blog.models import BetToReturn, Prediction

# タイムゾーン設定
JST = timezone(timedelta(hours=+9), 'JST')
today = datetime.now(JST)


class PredictionModelTest(TestCase):

    def test_is_empty(self):
        saved_post = Prediction.objects.all()
        self.assertEqual(saved_post.count(), 0)

    def test_is_count_one(self):
        post = Prediction(title='阪神11R', place="阪神", race_num=11, race_time=today,
                          horse_1=2, horse_2=3, horse_3=4, horse_4=5)
        post.save()
        saved_posts = Prediction.objects.all()
        self.assertEqual(saved_posts.count(), 1)

    def test_saving_and_retrieving_post(self):
        post = Prediction()
        title = '阪神11R'
        place = "阪神"
        race_num = 11
        race_time = today
        horse_1 = 2
        horse_2 = 3
        horse_3 = 4
        horse_4 = 5

        post.title = title
        post.place = place
        post.race_num = race_num
        post.race_time = race_time
        post.horse_1 = horse_1
        post.horse_2 = horse_2
        post.horse_3 = horse_3
        post.horse_4 = horse_4
        post.save()

        saved_post = Prediction.objects.all()
        actual_post = saved_post[0]

        self.assertEqual(actual_post.title, title)
        self.assertEqual(actual_post.place, place)


class BetToWinModelTest(TestCase):

    def test_is_empty(self):
        saved_post = Prediction.objects.all()
        self.assertEqual(saved_post.count(), 0)

    def test_is_count_one(self):
        post = BetToReturn(title='阪神11R', place="阪神", race_num=11, race_time=today,
                           bet=1000, payoff=2000, win=1000, win_show=1000,
                           result_one_win=2, result_two_win=4, result_thr_win=5, comment='')
        post.save()
        saved_posts = BetToReturn.objects.all()
        self.assertEqual(saved_posts.count(), 1)

    def test_saving_and_retrieving_post(self):
        title = '阪神11R'
        place = "阪神"
        race_num = 11
        race_time = today
        bet = 1000
        payoff = 2000
        win = 1000
        win_show = 1000
        result_one_win = 2
        result_two_win = 4
        result_thr_win = 5
        comment = ''

        post = BetToReturn()
        post.title = title
        post.place = place
        post.race_num = race_num
        post.race_time = race_time
        post.bet = bet
        post.payoff = payoff
        post.win = win
        post.win_show = win_show
        post.result_one_win = result_one_win
        post.result_two_win = result_two_win
        post.result_thr_win = result_thr_win
        post.comment = comment
        post.save()

        saved_post = BetToReturn.objects.all()
        actual_post = saved_post[0]

        self.assertEqual(actual_post.title, title)
        self.assertEqual(actual_post.place, place)






