from django import forms

from courses.models import Courses


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = [
            'title',
            'duration',
            'price',
            'image',
            'status',
            'lesson_duration',
            'weekday'
        ]



