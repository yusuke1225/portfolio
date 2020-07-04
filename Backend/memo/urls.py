from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'memo'


urlpatterns = [
    path('memo/', views.MemoView.as_view()),
    path('chara/', views.CharaView.as_view()),
    path('result/', views.ResultView.as_view())
]