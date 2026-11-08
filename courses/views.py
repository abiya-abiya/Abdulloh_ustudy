from django.shortcuts import render, get_object_or_404

from courses.models import Courses
from page.forms import ApplicationForm


# Create your views here.


def list_course(request):
    course = Courses.objects.all()
    context = {'course': course}
    return render(request, 'course/course_list.html', context)


def detail_course(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    context = {'course': course, 'form': ApplicationForm(initial={'course': course})}
    return render(request, 'course/course_detail.html', context)
