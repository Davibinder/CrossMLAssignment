from django.urls import path
from main_app.views.fileUpload import create_profile
from CrossMLAssignment import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', create_profile, name = 'create'),
]
