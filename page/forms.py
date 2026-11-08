import re

from django import forms

from page.models import Speakers, Branches, Application


class SpeakersForm(forms.ModelForm):
    class Meta:
        model = Speakers
        fields = [
            'first_name',
            'last_name',
            'description',
            'experience',
            'image',
            'course',
        ]


class ApplicationForm(forms.ModelForm):
    # Model 13 belgini saqlaydi (+998XXXXXXXXX), lekin foydalanuvchi bo'shliq/chiziqcha bilan yozishi mumkin
    phone = forms.CharField(max_length=25, label="Telefon raqami",
                            widget=forms.TextInput(attrs={'placeholder': '+998', 'type': 'tel'}))

    class Meta:
        model = Application
        fields = ['branch', 'course', 'full_name', 'phone']
        widgets = {
            'course': forms.HiddenInput,
            'full_name': forms.TextInput(attrs={'placeholder': 'Ism va familiya'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branches.objects.filter(is_active=True)
        self.fields['branch'].required = True
        self.fields['branch'].empty_label = 'Filial'

    def clean_phone(self):
        digits = re.sub(r'\D', '', self.cleaned_data['phone'])
        if len(digits) == 9:  # "90 123 45 67" ko'rinishida yozilgan bo'lsa
            digits = '998' + digits
        if not re.fullmatch(r'998\d{9}', digits):
            raise forms.ValidationError("Telefon raqamini +998 XX XXX XX XX ko'rinishida kiriting.")
        return '+' + digits
