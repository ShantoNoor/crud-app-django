from django.contrib import admin
from django.urls import path, include

from .views import *

app_name = 'to_do'

urlpatterns = [
    path('', to_do_list_view, name=f'{app_name}_list'),
    path('create/', to_do_create_view, name=f'{app_name}_create'),
    path('update/<int:pk>', to_do_update_view, name=f'{app_name}_update'),
    path('delete/<int:pk>', to_do_delete_view, name=f'{app_name}_delete'),
]
