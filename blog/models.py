from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

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


class BetToReturn(models.Model):
    title = models.CharField(max_length=100)
    place = models.DateTimeField(max_length=10)
    race_num = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    race_time = models.DateTimeField()
    bet = models.IntegerField()
    to_return = models.IntegerField()
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.title
