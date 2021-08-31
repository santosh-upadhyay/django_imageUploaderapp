from django.shortcuts import render
from .forms import imageForm
from .models import Image
# Create your views here.
def home(request):
    if request.method == "POST":
        fm = imageForm(request.POST,request.FILES)
        if fm.is_valid(): 
            fm.save() 
    else:
        fm = imageForm()
    img = Image.objects.all()
    return render(request, 'home.html',{'img':img,'fm':fm})