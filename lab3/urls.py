from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page1/', views.index, name='page1'),
    path('page2/', views.index, name='page2'),
]