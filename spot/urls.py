from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('spot/', views.index, name="yoyo"),
    path('spottrain/', views.view, name="view")

]
