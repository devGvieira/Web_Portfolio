from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('download_my_pdf', views.download_pdf, name="download_pdf")
]