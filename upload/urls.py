from django.urls import path
from upload import views

urlpatterns = [
    path('', views.upload_file, name='upload'),
]
