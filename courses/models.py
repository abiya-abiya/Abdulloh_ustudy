from django.db import models


class Courses(models.Model):
    FORMAT_CHOICES = [
        ('Oflayn', 'Oflayn'),
        ('Onlayn', 'Onlayn'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.IntegerField()  # oy
    weekday = models.IntegerField()  # haftada necha kun
    lesson_duration = models.IntegerField()  # akademik soat
    price = models.IntegerField()  # so'm, oyiga
    status = models.CharField(max_length=100, choices=FORMAT_CHOICES, default='Oflayn')
    min_age = models.PositiveSmallIntegerField(null=True, blank=True, help_text="Masalan 16 -> '16+ yoshdan'")
    # Quyidagi uchta maydon: har bir qatorga bitta band yoziladi
    target_audience = models.TextField(blank=True, help_text="Ushbu kurs kimlarga mos keladi? (har qatorda bitta)")
    what_you_learn = models.TextField(blank=True, help_text="Kursda nimani o'rganasiz? (har qatorda bitta)")
    skills = models.TextField(blank=True, help_text="Siz ega bo'ladigan ko'nikmalar (har qatorda bitta)")
    image = models.ImageField(upload_to='courses/images/', null=True, blank=True)
    video = models.FileField(upload_to='courses/videos/', null=True, blank=True)

    def __str__(self):
        return self.title
