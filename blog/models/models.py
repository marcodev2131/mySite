from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()

    def __str__(self):
        return self.title