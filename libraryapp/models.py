import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Address(models.Model):
    address_line_1 = models.CharField(max_length=75)
    address_line_2 = models.CharField(max_length=75, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    def __str__(self):
        return self.address_line_1 + " " + self.city + " " + self.state + " " + self.zip_code

class Library(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Member(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)    
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    join_date = models.DateTimeField('member since')
    def __str__(self):
        return self.first_name + " " + self.last_name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=75)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class BookAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return self.book.title + " - " + self.author.first_name + " " + self.author.last_name
