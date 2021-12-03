from django.contrib import admin
from .models import BetToReturn, Prediction

# Register your models here.
admin.site.register(BetToReturn)
admin.site.register(Prediction)