from django.urls import path
from main_app.views.fileUpload import create_profile

urlpatterns = [
    path('', create_profile, name = 'create'),
]
