from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.model_form_upload, name='uploads'),
    path('list-files/', views.arquivos, name='list_files'),
]
