from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name='info'),
    path('room_list/', views.RoomList.as_view(), name='room_list'),
    path('search_booking/', views.SearchBooking.as_view(), name='search_booking'),
    path('get_booking/<int:pk>', views.get_booking, name='get_booking'),
]
