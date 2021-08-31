from django import forms
from .models import Image

#forms
class imageForm(forms.ModelForm):
    class Meta:
        model = Image
        #fields =('image',)
        fields = '__all__'
        labels = {'image':''}

    
