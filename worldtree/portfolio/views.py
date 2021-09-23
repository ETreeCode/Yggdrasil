import os
import dotenv
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Add .env variables anywhere before SECRET_KEY
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# UPDATE secret key
PDF_API_ID = os.environ['DEV_PDF_API_ID'] # Instead of your actual secret key

from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def resume(request):
    context = {"pdf": PDF_API_ID}
    return render(request, 'portfolio/resume.html', context)
