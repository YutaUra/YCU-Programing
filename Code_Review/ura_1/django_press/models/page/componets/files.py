from django.db import models


class ImageFile(models.Model):
    file = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Image {self.name}'
