from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('predict/', views.predict, name='predict'),
    path('predict/detail/<int:pk>/', views.detail_predict_post, name='detail_predict'),
    path('predict/detail/result/<int:pk>/', views.detail_predict_result, name='detail_predict_result'),
    path('contact/', views.contact, name='contact'),
    path('complete/', views.complete, name='complete')
]