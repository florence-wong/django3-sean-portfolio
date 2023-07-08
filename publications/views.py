from django.shortcuts import render
from .models import Publication

# Create your views here.
def all_publications(request):
    publications=Publication.objects.all()
    return render(request,'publications/all_publications.html',{'publications':publications})