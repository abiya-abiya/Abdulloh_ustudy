from django.shortcuts import render, redirect

from page.forms import SpeakersForm


# Create your views here.


def home(request):
    return render(request, 'home/home.html')

def about_us(request):
    return render(request, 'about-us/about-us.html')

def contact_us(request):
    return render(request, 'contacts/contacts.html')
def news(request):
    return render(request, 'news/news.html')

def create_speakers(request):
    if request.method == 'POST':
        form = SpeakersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = SpeakersForm()
    context = {'form': form}
    return render(request, 'speakers/speakers.html', context)

