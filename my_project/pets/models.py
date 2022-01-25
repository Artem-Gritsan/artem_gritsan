from django.db import models
from django.db.models.expressions import Func
from django.db.models.fields import CharField

class Author(models.Model):
    name = models.CharField(blank=False, max_length=30)
    email = models.EmailField(blank=False, primary_key=True, max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name}'

class Post(models.Model):
    PET_TYPES = [('c', 'cat'), ('d', 'dog')]
    pet_type = models.CharField(choices=PET_TYPES, max_length=1, blank=False, default='c')
    title = models.CharField(blank=False, max_length=40)
    content = models.TextField(blank=False, max_length=400)
    breed = models.CharField(blank=False, max_length=30)
    сontact_person = models.CharField(blank=False, max_length=30)
    tel = models.CharField(blank=False, max_length=13)
    locality = models.CharField(blank=False, max_length=30)
    price = models.CharField(blank=False, max_length=20)
    image = models.ImageField(upload_to = 'uploads')
    issued = models.DateTimeField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}'


