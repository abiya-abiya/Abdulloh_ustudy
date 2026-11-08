from courses.models import Courses


def footer(request):
    # Lazy queryset: faqat footer render bo'lganda bitta so'rov ketadi
    return {'footer_courses': Courses.objects.only('id', 'title')[:6]}
