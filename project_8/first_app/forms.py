from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ['username', 'first_name', 'last_name', 'email']

class DataChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
