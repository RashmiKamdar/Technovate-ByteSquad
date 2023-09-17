from django.shortcuts import render
from .models import ImageModel
# Create your views here.

def display_image(request, image_id):
    try:
        image_model = ImageModel.objects.get(pk=image_id)
    except ImageModel.DoesNotExist:
        image_model = None

    return render(request, 'image.html', {'image_model': image_model})