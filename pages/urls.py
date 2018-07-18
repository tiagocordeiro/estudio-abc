from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quem-somos/', views.about, name='about-us'),
    path('contato/', views.contact, name='contact'),
    path('contato/obrigado/', views.success, name='success')
]
