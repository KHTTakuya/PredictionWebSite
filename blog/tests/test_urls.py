from datetime import timezone, timedelta, datetime

from django.test import TestCase
from django.urls import resolve
from blog.views import index, about, contact, predict, detail_predict_post
from blog.models import Prediction

# タイムゾーン設定
JST = timezone(timedelta(hours=+9), 'JST')
today = datetime.now(JST)


class TestUrls(TestCase):

    def test_index_url(self):
        view = resolve('/')
        self.assertEqual(view.func, index)

    def test_about_url(self):
        view = resolve('/about/')
        self.assertEqual(view.func, about)

    def test_contact_url(self):
        view = resolve('/contact/')
        self.assertEqual(view.func, contact)

    def test_predict_url(self):
        view = resolve('/predict/')
        self.assertEqual(view.func, predict)

