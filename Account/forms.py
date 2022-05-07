from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from Account.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address")

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        msg = 'Special symbols such as @, +, /, ! and numbers are not allowed in a name. Please use only alphabets and/or . and -.'
        regex = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 '0', '"']
        for i in regex:
            if i in first_name:
                self.add_error('first_name', msg)

        for i in regex:
            if i in last_name:
                self.add_error('last_name', msg)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")


class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login")
