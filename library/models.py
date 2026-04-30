from django.db import models

# Create your models here.
class Author (models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField( unique=True )
    bio = models.TextField(blank=True)
    
    
class Book(models.Model):
    title = models.CharField( max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField( max_length=50)
    pubished_date = models.DateField()
    total_copies = models.IntegerField(default=1)
    available_copies = models.IntegerField(default=1)
    
class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    joined_at = models.DateTimeField( auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
class BorrowRecord(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrwed_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    returned_at = models.DateTimeField(auto_now_add=True)
    is_returned = models.BooleanField(default=False)