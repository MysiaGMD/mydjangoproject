from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Books


def book_list(request):
    books = Books.objects.all()  

    return render(request, 'books/book_list.html', {'books': books})


def book_detail(request, book_id):

    book = get_object_or_404(Books, id=book_id)

    return render(request, 'books/book_detail.html', {'book': book})


def search_books(request):
    query = request.GET.get('q', '') 
    query = query.strip().lower()  

    if query:
        words = query.split() 
        filters = Q() 

        for word in words:
            filters |= Q(title__icontains=word)  

        books = Books.objects.filter(filters)  
    else:
        books = []

    return render(request, 'books/search.html', {'books': books})