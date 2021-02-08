from django import forms
from .models import WildLife


class ImageForm(forms.ModelForm):
    class Meta: #connect model to form
        model=WildLife
        fields=('img',)


