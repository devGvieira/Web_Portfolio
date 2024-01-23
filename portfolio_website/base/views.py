from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os

def home(request):
    return render(request, 'base/home.html')

def download_pdf(request):
    filename = 'staticfiles/files/CV.pdf'
    with open(filename, 'rb') as pdf_file:
        content = FileWrapper(pdf_file)
        response = HttpResponse(content, content_type='application/pdf')
        response['Content-Length'] = os.path.getsize(filename)
        response['Content-Disposition'] = 'attachment; filename=%s' % 'CV.pdf'
    return response