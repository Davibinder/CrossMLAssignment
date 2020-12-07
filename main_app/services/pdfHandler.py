import PyPDF2

def getPdfRawText(pdfFile):
    textData = ""
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    number_of_pages = pdfReader.getNumPages()
    for page_number in range(number_of_pages):
        page = pdfReader.getPage(page_number)
        textData += page.extractText()

    print(pdfReader.numPages)
    return textData