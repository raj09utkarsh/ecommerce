from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class UserRegisterForm(forms.ModelForm):
#     password = forms.CharField(widget = forms.PasswordInput, label = 'Password')
#     password2 = forms.CharField(widget = forms.PasswordInput, label = 'Confirm Password')

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', ]
#         def clean_password2(self):
#             cd = self.cleaned_data
#             if cd['password'] != cd['password2']:
#                 raise forms.ValidationError("Both password don't match.")
#             return cd['password2']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name',]