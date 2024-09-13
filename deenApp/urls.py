from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('question/', views.question, name='question'),
    path('instructions/', views.instructions, name='instructions'),
    path('communication/', views.communication, name='communication'),
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signup, name='signup'),
    path('biodata/', views.biodata, name='biodata'),
]