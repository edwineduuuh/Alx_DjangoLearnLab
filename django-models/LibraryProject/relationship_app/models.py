from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    class Meta:
        ordering = ['title']

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Libraries"
        ordering = ['name']

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, 
                                   on_delete=models.CASCADE,
                                   related_name='librarian')
    
    def __str__(self):
        return f"{self.name} (Librarian at {self.library.name})"
    
    class Meta:
        ordering = ['name']