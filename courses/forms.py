from django import forms

from courses.models import Courses


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = [
            'title',
            'description',
            'duration',
            'price',
            'image',
            'video',
            'status',
            'min_age',
            'lesson_duration',
            'weekday',
            'target_audience',
            'what_you_learn',
            'skills',
        ]
