from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.info, name='info'),
    # path('room_list/', views.RoomList.as_view(), name='room_list'),
    path('search_booking/', views.SearchBooking.as_view(), name='search_booking'),
    path('room_list/', views.CreateBooking.as_view(), name='create_booking'),
    path('contact/', views.CreateContact.as_view(), name='create_contact'),
    path('review/', views.CreateReview.as_view(), name='create_review'),
]
