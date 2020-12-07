from django import forms
from main_app.models.fileUpload import File_Upload
#DataFlair #File_Upload
class Upload_Form(forms.ModelForm):
    class Meta:
        model = File_Upload
        fields = [
        'pdfFile'
        ]