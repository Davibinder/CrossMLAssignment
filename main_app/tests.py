from django.test import TestCase
from main_app.services.wordTagGenerator import genrateWordTagsFromText
from main_app.services.pdfHandler import getPdfRawText
from django.conf import settings

# Create your tests here.

class GenralTest(TestCase):

    def test_testWordCloudService(self):
        base64Data = genrateWordTagsFromText('aa bb cc  aa aa aa aa aa')
        self.assertTrue(base64Data)

    def test_extractrawTextFromPdf(self):
        rawText = getPdfRawText(settings.MEDIA_ROOT+'/example.pdf')
        self.assertTrue(rawText)