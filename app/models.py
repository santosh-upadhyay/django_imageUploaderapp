from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = "media/myimage")
    date = models.DateTimeField(auto_now_add = True)

