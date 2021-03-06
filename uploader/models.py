from django.db import models
from django.utils.timezone import now

# Create your models here.

class Upload(models.Model):
	caption = models.CharField(default="File", max_length=200)
	date_added = models.DateField(default=now())
	file = models.FileField(upload_to= "uploads/%d-%m-%y", default=None)

	def __str__(self):
		return self.caption
