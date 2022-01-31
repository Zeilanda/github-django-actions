from django.contrib.auth.forms import UserCreationForm

from calendar_auth.models import CalendarUser


class CalendarUserCreateForm(UserCreationForm):

    class Meta:
        model = CalendarUser
        fields = ('username', 'email', 'password1', 'password2')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field_obj in self.fields.items():
