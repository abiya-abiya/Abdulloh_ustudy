from django.shortcuts import render

from courses.models import Courses


# Create your views here.


def list_course(request):
    course = Courses.objects.all()
    context = {'course': course}
    return render(request, 'course/course_list.html', context)



