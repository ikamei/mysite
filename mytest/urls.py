# urls.py --- 
# Filename: urls.py
# Created: 六  6 27 20:55:46 2020 (+0800)
# 
# 
# Copyright Weiguo Mao All Rights Reserved.
# 
# 
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:machine_id>/<str:active_time>/<str:scene_name>/<int:text_index>/', views.save_keyrecord, name='save_keyrecord'),
]
