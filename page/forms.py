from django import forms

from page.models import Speakers


class SpeakersForm(forms.ModelForm):
    class Meta:
        model = Speakers
        fields = [
            'first_name',
            'last_name',
            'description',
            'experience',
        ]