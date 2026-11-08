from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from page.forms import SpeakersForm, ApplicationForm
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

@require_POST
def apply(request):
    form = ApplicationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Arizangiz qabul qilindi! Tez orada siz bilan bog'lanamiz.")
    else:
        # shortcut: xatolar flash-xabar bo'lib chiqadi, maydon yonida emas; kerak bo'lsa formani qayta render qilish kerak
        messages.error(request, " ".join(e for errs in form.errors.values() for e in errs))
    next_url = request.POST.get('next', '')
    if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
        next_url = 'home'
    return redirect(next_url)
