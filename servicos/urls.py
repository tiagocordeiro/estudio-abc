from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/servicos/', views.servicos_list, name='servicos_list'),
]
