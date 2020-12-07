from django.shortcuts import render
from main_app.forms.uploadFile import Upload_Form
from main_app.services.pdfHandler import getPdfRawText
from main_app.services.wordTagGenerator import genrateWordTagsFromText

IMAGE_FILE_TYPES = ['pdf']

def upload_file(request):
    form = Upload_Form()
    if request.method == 'POST':
        form = Upload_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.pdfFile = request.FILES['pdfFile']
            file_type = user_pr.pdfFile.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'error.html')
            # user_pr.save()
            text = getPdfRawText(user_pr.pdfFile)
            imageData = genrateWordTagsFromText(text)
            return render(request, 'details.html', {'user_pr': user_pr,'text':text,'imgData':imageData})
    context = {"form": form,}
    return render(request, 'create.html', context)
