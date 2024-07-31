from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),
    # path('add/',views.add_person ),
    path('add/',views.add_item ),
    # path('show/',views.get_all_persons ),
    path('show/',views.get_all_items ),
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('add_person/', views.add_person, name='add_person'),
#     path('get_all_persons/', views.get_all_persons, name='get_all_persons'),
# ]
