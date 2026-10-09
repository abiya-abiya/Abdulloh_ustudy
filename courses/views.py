from django.shortcuts import render

from courses.models import Courses


# Create your views here.


def list_course(request):
    course = Courses.objects.all()
    context = {'course': course}
    return render(request, 'course/course_list.html', context)


def detail_course(request, pk):
    course = Courses.objects.get(pk=pk)
    context = {'course': course}
    return render(request, 'course/course_detail.html', context)
