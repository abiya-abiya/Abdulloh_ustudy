from django.test import TestCase
from django.urls import reverse

from courses.models import Courses


class CourseDetailTests(TestCase):
    def test_missing_course_is_404(self):
        self.assertEqual(self.client.get(reverse('detail_course', args=[999])).status_code, 404)

    def test_detail_shows_description_sections_and_form(self):
        c = Courses.objects.create(title="Backend", description="Django o'rganamiz", duration=12, weekday=3,
                                   lesson_duration=2, price=2000000, min_age=16, skills="Django\nDocker")
        r = self.client.get(reverse('detail_course', args=[c.pk]))
        self.assertContains(r, "Django o&#x27;rganamiz")
        self.assertContains(r, "16+ yoshdan")
        self.assertContains(r, "<li>Docker</li>", html=True)
        self.assertContains(r, 'id="apply"')
        self.assertContains(r, f'value="{c.pk}"')
