from django.db import models


# Create your models here.
class Publication(models.Model):
    title=models.CharField(max_length=400)
    description=models.CharField(max_length=450)
    image=models.ImageField(upload_to="portfolio/images/")
    url=models.URLField(blank=True)

    def __str__(self):
        return self.title