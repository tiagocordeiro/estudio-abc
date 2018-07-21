from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/servicos/', views.servicos_list, name='servicos_list'),
    path('dashboard/servicos/upload/fotolito/', views.fotolito_upload,
         name='upload_fotolito'),
]
