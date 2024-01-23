from django.shortcuts import render
from .models import MyModel
from .forms import ImageUploadForm

# Create your views here.

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageUploadForm()
    return render(request, 'index.html', {'form': form})

def photos_views(request):
    photos = MyModel.objects.all()  # Retrieve all photos from your model
    return render(request, 'image.html', {'photos': photos})