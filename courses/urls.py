from django.urls import path

from courses.views import list_course, detail_course

urlpatterns = [
    path('list_course/', list_course, name='list_course'),
    path('detail_course/<int:pk>/', detail_course, name='detail_course'),

]