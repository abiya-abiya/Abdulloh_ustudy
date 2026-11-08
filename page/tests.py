from django.test import TestCase
from django.urls import reverse

from courses.models import Courses
from page.models import Application, Branches, News


class ApplyTests(TestCase):
    def setUp(self):
        self.branch = Branches.objects.create(name="IT Park", address="Toshkent", latitude=41.3, longitude=69.3)
        self.course = Courses.objects.create(title="Backend", duration=12, weekday=3, lesson_duration=2, price=2000000)

    def post(self, **data):
        payload = {'branch': self.branch.pk, 'full_name': 'Ali Valiyev', 'phone': '+998 90 123-45-67', **data}
        return self.client.post(reverse('apply'), payload, follow=True)

    def test_valid_application_saved_with_normalized_phone(self):
        r = self.post(course=self.course.pk, next=reverse('detail_course', args=[self.course.pk]))
        app = Application.objects.get()
        self.assertEqual(app.phone, '+998901234567')
        self.assertEqual(app.course, self.course)
        self.assertContains(r, "Arizangiz qabul qilindi")

    def test_nine_digit_phone_gets_country_code(self):
        self.post(phone='90 123 45 67')
        self.assertEqual(Application.objects.get().phone, '+998901234567')

    def test_bad_phone_rejected(self):
        r = self.post(phone='12345')
        self.assertFalse(Application.objects.exists())
        self.assertContains(r, "+998 XX XXX XX XX")

    def test_inactive_branch_rejected(self):
        self.branch.is_active = False
        self.branch.save()
        self.post()
        self.assertFalse(Application.objects.exists())

    def test_external_next_ignored(self):
        r = self.client.post(reverse('apply'), {'branch': self.branch.pk, 'full_name': 'A', 'phone': '901234567', 'next': 'https://evil.com/'})
        self.assertRedirects(r, reverse('home'), fetch_redirect_response=False)

    def test_get_not_allowed(self):
        self.assertEqual(self.client.get(reverse('apply')).status_code, 405)


class HomeTests(TestCase):
    def test_home_shows_courses_speakers_and_form(self):
        Courses.objects.create(title="Frontend", duration=12, weekday=3, lesson_duration=2, price=2000000)
        r = self.client.get(reverse('home'))
        self.assertContains(r, "Frontend")
        self.assertContains(r, "Nega aynan Ustudy?")
        self.assertContains(r, 'id="apply"')
        self.assertContains(r, f'action="{reverse("apply")}"')

    def test_home_without_data_still_renders(self):
        r = self.client.get(reverse('home'))
        self.assertEqual(r.status_code, 200)
        self.assertNotContains(r, "O'z kursingizni tanlang")



class PagesTests(TestCase):
    def test_news_list_and_home_show_only_published(self):
        News.objects.create(title="Hackathon", body="Matn")
        News.objects.create(title="Qoralama", body="Matn", is_published=False)
        for url in (reverse('news'), reverse('home')):
            r = self.client.get(url)
            self.assertContains(r, "Hackathon")
            self.assertNotContains(r, "Qoralama")

    def test_news_detail(self):
        n = News.objects.create(title="Hackathon", body="Birinchi abzats")
        draft = News.objects.create(title="Qoralama", body="x", is_published=False)
        self.assertContains(self.client.get(reverse('news_detail', args=[n.pk])), "Birinchi abzats")
        self.assertEqual(self.client.get(reverse('news_detail', args=[draft.pk])).status_code, 404)

    def test_about_and_contacts_have_form(self):
        Branches.objects.create(name="Nukus - IT Park", address="Nukus", latitude=42.4, longitude=59.6)
        about = self.client.get(reverse('about_us'))
        self.assertContains(about, "Biz haqimizda")
        self.assertContains(about, 'id="apply"')
        contacts = self.client.get(reverse('contacts'))
        self.assertContains(contacts, "Nukus - IT Park", count=2)  # filial kartochkasi + formadagi variant
        self.assertContains(contacts, 'id="apply"')
