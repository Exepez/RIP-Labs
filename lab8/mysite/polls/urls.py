from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('i7-10700k/', views.cpu1, name='cpu1'),
    path('i9-10900k/', views.cpu2, name='cpu2'),
    path('ryzen-7-3800x/', views.cpu3, name='cpu3'),
]