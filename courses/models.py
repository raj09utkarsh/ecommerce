from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(default = 'default_course.jpg',upload_to = 'course')
    description = models.TextField()
    dateAdded = models.DateTimeField(auto_now_add=True)
    coursePrice = models.IntegerField()
    eligibility = models.CharField(max_length = 200)
    aims = models.TextField()
    classScheduling = models.TextField()
    courseCompletion = models.TextField()

    def __str__(self):
        return self.title

class Order(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null = True)
    buyer  = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return f"{self.buyer} bought {self.course} course"