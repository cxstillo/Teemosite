from fileinput import filename
from django.db import models

# Create your models here.
class gallery(models.Model):
    image= models.FileField(upload_to='images/',null=True)
    filename= models.CharField(max_length=225,null=True, blank=True)

    def __str__(self) -> str:
        return str(self.filename)