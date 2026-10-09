from django.db import models

# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    weekday = models.IntegerField()
    lesson_duration = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.title