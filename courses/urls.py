from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contactUs, name='contact'),
    path('<int:course_id>/', views.courseDetail, name='detail'),
    path('<int:course_id>/buy/', views.buyProduct, name='buyProduct'),
]
