from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    img_src = models.URLField(blank=True, null=True)
    years_of_age = models.CharField(max_length=9)
    bio = models.TextField()
    works = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'author'  
        ordering = ['name']  

    def __str__(self): 
        return self.name



class Books(models.Model):
    title = models.CharField(max_length=200)     
    author_name = models.CharField(max_length=100) 
    price = models.IntegerField()                

    class Meta:
        db_table = 'book'      
        ordering = ['title'] 

    def __str__(self):
        return self.title



class BookDetail(models.Model):
    isbn = models.CharField(max_length=20)         
    pages = models.IntegerField()                  
    publisher = models.CharField(max_length=100)   

    class Meta:
        db_table = 'book_detail' 

    def __str__(self):
        return self.isbn
