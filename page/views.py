from django.shortcuts import render, redirect

from page.forms import SpeakersForm
from page.models import Speakers, Branches


# Create your views here.


def home(request):
    return render(request, 'home/home.html')

def about_us(request):
    return render(request, 'about-us/about-us.html')

def contact_us(request):
    return render(request, 'contacts/contacts.html')
def news(request):
    return render(request, 'news/news.html')

# def create_speakers(request):
#     if request.method == 'POST':
#         form = SpeakersForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#     else:
#         form = SpeakersForm()
#     context = {'form': form}
#     return render(request, 'speakers/speakers.html', context)

def list_speakers(request):
    speakers = Speakers.objects.all()
    context = {'speakers': speakers}
    return render(request, 'speakers/list_speakers.html', context)


def list_branches(request):
    branches = Branches.objects.filter(is_active=True)
    context = {'branches': branches}
    return render(request, 'branches/branches.html', context)
# def