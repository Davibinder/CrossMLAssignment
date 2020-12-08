from django.test import TestCase, Client
from main_app.services.wordTagGenerator import genrateWordTagsFromText
from main_app.services.pdfHandler import getPdfRawText
from django.conf import settings

# Create your tests here.

class GenralTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_testWordCloudService(self):
        base64Data = genrateWordTagsFromText('aa bb cc  aa aa aa aa aa')
        self.assertTrue(base64Data)

    def test_extractrawTextFromPdf(self):
        rawText = getPdfRawText(settings.MEDIA_ROOT+'/example.pdf')
        self.assertTrue(rawText)

    def test_homepage(self):
        homepage = self.client.get('')
        self.assertTrue(homepage.status_code, 200)
        self.assertTemplateUsed(homepage, 'upload.html')