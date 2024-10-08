from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=500)
    category = models.CharField(max_length=255, null=True, blank=True)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
