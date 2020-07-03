from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from courses.models import Order
from . import forms

@login_required
def Profile(request):
    # user_id = request.user.pk
    enrolled_courses = Order.objects.filter(buyer = request.user)
    return render(request, 'accounts/profile.html', {'enrolled_courses': enrolled_courses})

def RegisterUser(request):
    if request.method == 'POST':
        user_register_form = forms.UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            # username = user_register_form.cleaned_data['username']
            user_register_form.save()
            return redirect('login')
    else:
        user_register_form = forms.UserRegisterForm()
    return render(request, 'registration/register.html', {'user_form': user_register_form})