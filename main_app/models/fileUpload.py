from django.db import models

class File_Upload(models.Model):
    pdfFile = models.FileField()
    def __str__(self):
        return self.pdfFile.url