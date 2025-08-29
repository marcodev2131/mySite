from django.db import models
from django.contrib.auth.models import User
import django


STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


# Exemplo de modelo
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    #Username (leave blank to use 'marco'): 
    #Email address: marco@admin.com


def test_django_version():
    assert django.get_version() == '5.2.5'