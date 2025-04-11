from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=300)  # Increased from 200 to 300
    description = models.TextField()
    # technologies = models.CharField(max_length=500)  # To hold multiple tech names
    # github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    tags = models.CharField(max_length=300, blank=True)  # Increased from 100 to 300
    # image = models.ImageField(upload_to='project_images/', blank=True)

    def __str__(self):
        return self.title
