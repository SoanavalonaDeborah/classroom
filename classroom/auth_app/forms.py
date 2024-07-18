from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        (1, 'Enseignant'),
        (2, 'Étudiant'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect())

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'user_type')

   
