import io
import PyPDF2
from django.shortcuts import render
from main_app.forms.uploadFile import Profile_Form

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
                return render(request, 'main_app/error.html')
            user_pr.save()
            testPdfText(user_pr.display_picture)
            return render(request, 'main_app/details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'main_app/create.html', context)

def testPdfText(pdfFile):
    # pdfFileObj = open(pdfFile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    # printing number of pages in pdf file
    print(pdfReader.numPages)
    # creating a page object
    pageObj = pdfReader.getPage(0)
    # extracting text from page
    print(pageObj.extractText())
    # closing the pdf file object
    # pdfFileObj.close()