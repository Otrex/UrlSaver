from django.db import models
from django.utils.timezone import now
# Create your models here.

class Urls (models.Model):
    url = models.TextField(default = None)
    url_details = models.TextField(default = None)
    url_thumb = models.TextField(default = "default.jpg")
    url_title = models.CharField(max_length = 200, default='None')
    date_inserted = models.DateField(default=now())
    date_modified = models.DateField(default=now())
