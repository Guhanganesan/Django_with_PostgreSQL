from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

class Profile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    biography = models.TextField()

    def __str__(self):
        return f'Profile of {self.author.name}'

