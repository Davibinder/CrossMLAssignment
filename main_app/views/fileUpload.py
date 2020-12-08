import asyncio
from django.shortcuts import render
from main_app.forms.fileUpload import Upload_Form
from main_app.services.pdfHandler import getPdfRawText
from main_app.services.wordTagGenerator import genrateWordTagsFromText

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

SUPPORTED_FILES = ['pdf']

async def upload_file(request):
    form = Upload_Form()
    if request.method == 'POST':
        form = Upload_Form(request.POST, request.FILES)
        if form.is_valid():
            fileObj = form.save(commit=False)
            fileObj.pdfFile = request.FILES['pdfFile']
            file_type = fileObj.pdfFile.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in SUPPORTED_FILES:
                return render(request, 'error.html')
            # fileObj.save()
            text = getPdfRawText(fileObj.pdfFile)
            imageData = genrateWordTagsFromText(text)
            return render(request, 'wordsTag.html', {'fileObj': fileObj,'text':text,'imgData':imageData})
    context = {"form": form,}
    return render(request, 'upload.html', context)
