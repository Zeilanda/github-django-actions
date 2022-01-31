from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

import calendar_auth.views as calendar_auth

urlpatterns = [
    path('user/create/',
         calendar_auth.CalendarUserCreateView.as_view(),
         name='user_create'),
    # path('cards/', cards.cards_list),
    path('login/',
         LoginView.as_view(),
         name='login'),
    path('logout/',
         LogoutView.as_view(),
         name='logout'),
]
