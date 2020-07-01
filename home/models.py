from django.db import models

# Create your models here.


class CNet(models.Model):
    """docstring for CNet"""
    title = models.CharField(max_length=500)
    img = models.URLField(default='#')
    href = models.CharField(max_length=999)
    content = models.TextField()

    def __str__(self):
        return (self.title)
