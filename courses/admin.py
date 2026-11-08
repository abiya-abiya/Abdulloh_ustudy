from django.contrib import admin

from courses.models import Courses


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'duration', 'price', 'min_age')
    list_filter = ('status',)
    search_fields = ('title',)
