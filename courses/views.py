from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Course
from .forms import ContactForm

# Create your views here.
def homePage(request):
    latest_courses = Course.objects.order_by('-dateAdded')[:5]
    courses_list = Course.objects.all()
    paginator = Paginator(courses_list, 9)
    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)
    return render(request, 'courses/main.html', {'courses': courses, 'page': page, 'latest_courses': latest_courses, 'title': 'homePage'})

def courseDetail(request, course_id):
    course = Course.objects.get(pk = course_id)
    return render(request, 'courses/detail.html', {'course': course})

def about(request):
    return render(request, 'courses/about.html', {'title': 'about'})

def contactUs(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data['your_name']
            userEmail = form.cleaned_data['email']
            message = f"This email is received from: {userName} {userEmail}: \nFeedback: {form.cleaned_data['message']}"
            send_mail('User query or feedback', message, settings.EMAIL_HOST_USER, [settings.TO_EMAIL], fail_silently=False)
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'courses/contact2.html', {'form': form, 'title': 'contact'})

@login_required
def buyProduct(request, course_id):
    course = Course.objects.get(pk = course_id)
    return render(request, 'courses/checkoutConfirm.html', {'course': course})