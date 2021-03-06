from django.db import models
import uuid

# Create your models here.
class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Store(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name


