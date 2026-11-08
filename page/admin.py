from django.contrib import admin

from page.models import Speakers, Branches, Application


@admin.register(Speakers)
class SpeakersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'course', 'experience')
    list_filter = ('course',)
    search_fields = ('first_name', 'last_name')


@admin.register(Branches)
class BranchesAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'is_active')
    list_editable = ('is_active',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'branch', 'course', 'created_at', 'is_contacted')
    list_filter = ('is_contacted', 'branch', 'course', 'created_at')
    list_editable = ('is_contacted',)
    search_fields = ('full_name', 'phone')
    readonly_fields = ('created_at',)
