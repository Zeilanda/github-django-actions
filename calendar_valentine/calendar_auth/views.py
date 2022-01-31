from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from calendar_auth.forms import CalendarUserCreateForm
from calendar_auth.models import CalendarUser


class CalendarUserCreateView(CreateView):
    model = CalendarUser
    success_url = '/'
    form_class = CalendarUserCreateForm

