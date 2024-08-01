
from django.contrib import admin
from django.urls import path
from .views import add_item, get_all_items, update_item, delete_item
urlpatterns = [
    path('add/', add_item, name='add_item'),
    path('show/', get_all_items, name='get_all_items'),
    path('update/', update_item, name='update_item'),
    path('delete/', delete_item, name='delete_item'),
]
