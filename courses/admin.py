from django.contrib import admin
from .models import Course, Order

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'image', 'description', 'dateAdded')
    search_fields = ('title', )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'course', 'buyer')