from django.db import models

class Speakers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField()
    experience = models.TextField()
    image = models.ImageField(upload_to='speakers/', blank=True, null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Branches(models.Model):
    name = models.CharField(max_length=200, verbose_name="Filial nomi")  # Masalan: "Toshkent - Mirzo Ulug'bek - IT Park"
    address = models.TextField(verbose_name="Manzil")  # Masalan: "Toshkent shahar, Kattaxo'ja ko'cha..."
    latitude = models.FloatField(verbose_name="Kenglik (Latitude)")  # Masalan: 41.338525
    longitude = models.FloatField(verbose_name="Uzunlik (Longitude)")  # Masalan: 69.334530
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    def __str__(self):
        return self.name

