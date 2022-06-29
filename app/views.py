
from django.shortcuts import render
from .models import*
from django.conf import settings

# Create your views here.
def index(request):
    ratgallery=gallery.objects.all()
    context={
        "ratgallery": ratgallery,
        "media_url": settings.MEDIA_URL


    }
    return render(request,"app/index.html",context)
