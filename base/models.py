from django.db import models


class Files(models.Model):
    file = models.ImageField(upload_to="medai")

# Create your models here.
