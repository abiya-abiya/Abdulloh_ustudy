from django.db import migrations


def normalize_status(apps, schema_editor):
    # "oflayn"/"OFLAYN" -> "Oflayn", tanlov ro'yxatiga mos bo'lishi uchun
    Courses = apps.get_model('courses', 'Courses')
    for course in Courses.objects.all():
        fixed = course.status.strip().capitalize()
        course.status = fixed if fixed in ('Oflayn', 'Onlayn') else 'Oflayn'
        course.save(update_fields=['status'])


class Migration(migrations.Migration):
    dependencies = [
        ('courses', '0004_courses_description_courses_min_age_courses_skills_and_more'),
    ]

    operations = [
        migrations.RunPython(normalize_status, migrations.RunPython.noop),
    ]
