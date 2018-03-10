from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('traindays/', views.pnr, name='index'),
    path('pnrstatus', views.detail, name='status')

]
