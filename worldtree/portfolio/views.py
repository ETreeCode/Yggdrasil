from django.conf import settings
from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def resume(request):
    context = {"pdf": settings.PDF_API_ID}
    return render(request, 'portfolio/resume.html', context)
