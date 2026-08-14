from django.db import models

class Speakers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField()
    experience = models.TextField()



