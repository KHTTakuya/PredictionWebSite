import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class BetToReturn(models.Model):
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    race_num = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    race_time = models.DateTimeField()
    bet = models.IntegerField(default=800)
    payoff = models.IntegerField()
    win = models.IntegerField()
    win_show = models.IntegerField()
    result_one_win = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(18)])
    result_two_win = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(18)])
    result_thr_win = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(18)])
    # コメントは馬連・馬単・ワイド・3連複・3連単が当たった場合のみ記述すること。
    comment = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class Prediction(models.Model):
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    race_num = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    race_time = models.DateTimeField()
    horse_1 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(18)])
    horse_2 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(18)])
    horse_3 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(18)])
    horse_4 = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(18)])
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
