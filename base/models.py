from django.db import models


class Files(models.Model):
    file = models.FileField(upload_to="images")

# Create your models here.
