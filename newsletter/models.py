from django.db import models

# Create your models here.
from django.db import models

class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='newsletter_images/')
    link = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

