from django.shortcuts import render
from main_app.forms.uploadFile import Profile_Form
from main_app.services.pdfHandler import getPdfRawText
from main_app.services.wordTagGenerator import genrateWordTagsFromText

IMAGE_FILE_TYPES = ['pdf']

def create_profile(request):
    form = Profile_Form()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'error.html')
            # user_pr.save()
            text = getPdfRawText(user_pr.display_picture)
            imageData = genrateWordTagsFromText(text)
            return render(request, 'details.html', {'user_pr': user_pr,'text':text,'imgData':imageData})
    context = {"form": form,}
    return render(request, 'create.html', context)
