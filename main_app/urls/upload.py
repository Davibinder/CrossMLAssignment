from django.urls import path
from main_app.views.fileUpload import upload_file

urlpatterns = [
    path('', upload_file, name = 'upload'),
]
