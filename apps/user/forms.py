from django.forms import ModelForm
from django.contrib.auth.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']