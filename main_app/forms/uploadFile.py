from django import forms
from main_app.models.fileUpload import User_Profile
#DataFlair #File_Upload
class Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = [
        'display_picture'
        ]