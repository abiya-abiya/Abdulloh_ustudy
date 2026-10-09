from django.urls import path

from courses.views import list_course

urlpatterns = [
    path('list_course/', list_course, name='list_course'),
]