from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from page.forms import SpeakersForm, ApplicationForm
from courses.models import Courses
from page.models import Speakers, Branches, News


# Create your views here.


# Bosh sahifadagi doimiy bloklar. Tez-tez o'zgarsa, model qilib admin'ga chiqarish mumkin
ROADMAP = [
    ("Kasbga kirish", "Soha atamalari, asosiy vositalar va mutaxassisning ish kuni bilan tanishasiz."),
    ("Texnik stek", "Asosiy texnologiyalarni chuqur o'rganib, mentor nazoratida dastlabki mashqlarni bajarasiz."),
    ("Real keyslar", "Bozordagidek vazifalar ustida ishlaysiz: dedlayn, texnik topshiriq, jamoaviy ish."),
    ("Portfolio", "Eng yaxshi ishlaringizni keys qilib rasmiylashtirasiz va ularni taqdim etishni o'rganasiz."),
    ("Karyera boshlanishi", "Rezyume, suhbatga tayyorgarlik va ish qidirish bo'yicha maslahatlar olasiz."),
]

ADVANTAGES = [
    ("🎓", "Dual ta'lim", "Nazariy darslar real loyihalardagi amaliyot bilan birga olib boriladi."),
    ("🏢", "Kompaniyada stajirovka", "Haqiqiy jamoada ishlab, bilimlaringizni amalda qo'llaysiz."),
    ("💼", "Ishga joylashish", "Eng yaxshi bitiruvchilarga hamkor kompaniyalarda ish taklif qilinadi."),
    ("⚙️", "Avtomatlashtirilgan ta'lim", "Platforma progressingizni kuzatib, dasturni sur'atingizga moslaydi."),
    ("💰", "Birinchi daromad", "Stajirovka davomida real loyihalar uchun haq olasiz."),
    ("📁", "Real portfolio", "Portfolio o'quv topshiriqlaridan emas, tijorat loyihalaridan yig'iladi."),
]


def home(request):
    context = {
        'roadmap': ROADMAP,
        'advantages': ADVANTAGES,
        'courses': Courses.objects.all()[:8],
        'speakers': Speakers.objects.select_related('course')[:8],
        'news_list': News.objects.filter(is_published=True)[:4],
        'form': ApplicationForm(),
    }
    return render(request, 'home/home.html', context)

def about_us(request):
    context = {'roadmap': ROADMAP, 'advantages': ADVANTAGES, 'form': ApplicationForm()}
    return render(request, 'about-us/about-us.html', context)

def contact_us(request):
    context = {'branches': Branches.objects.filter(is_active=True), 'form': ApplicationForm()}
    return render(request, 'contacts/contacts.html', context)
def news(request):
    # shortcut: sahifalash yo'q, yangiliklar ko'payib ketsa Paginator qo'shish kerak
    context = {'news_list': News.objects.filter(is_published=True)}
    return render(request, 'news/news.html', context)


def news_detail(request, pk):
    item = get_object_or_404(News, pk=pk, is_published=True)
    return render(request, 'news/news_detail.html', {'item': item})

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
    speakers = Speakers.objects.select_related('course')
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
