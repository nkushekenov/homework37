from django import forms
from .models import MyModel

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['image']
