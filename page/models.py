from django.db import models

class Speakers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField()
    experience = models.TextField()
    image = models.ImageField(upload_to='speakers/', blank=True, null=True)
    course = models.ForeignKey('courses.Courses', on_delete=models.SET_NULL, null=True, blank=True, related_name='speakers')
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



class Application(models.Model):
    """'Bepul darsga yoziling' / 'Kursga yozilish' formasidan kelgan ariza."""
    branch = models.ForeignKey(Branches, on_delete=models.SET_NULL, null=True, verbose_name="Filial")
    course = models.ForeignKey('courses.Courses', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kurs")
    full_name = models.CharField(max_length=150, verbose_name="Ism va familiya")
    phone = models.CharField(max_length=13, verbose_name="Telefon raqami")
    is_contacted = models.BooleanField(default=False, verbose_name="Bog'lanildimi?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Ariza"
        verbose_name_plural = "Arizalar"

    def __str__(self):
        return f"{self.full_name} ({self.phone})"


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    body = models.TextField(verbose_name="Matn")
    image = models.ImageField(upload_to='news/', blank=True, null=True, verbose_name="Rasm")
    is_published = models.BooleanField(default=True, verbose_name="Chop etilganmi?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Sana")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

    def __str__(self):
        return self.title
