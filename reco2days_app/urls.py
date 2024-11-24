
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_track, name='search_track'),
    path('add/', views.add_track, name='add_track'),
    path('list/', views.get_track_list, name='get_track_list'),
]