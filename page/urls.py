from django.urls import path

from page import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about-us/", views.about_us, name="about_us"),
    path("contacts/", views.contact_us, name="contacts"),
    path("news/", views.news, name="news"),
    path("speakers/", views.list_speakers, name="list_speakers"),
    path("list_branches/", views.list_branches, name="list_branches"),
]