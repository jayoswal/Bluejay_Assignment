from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display/', views.display_data, name='display_data')
]
