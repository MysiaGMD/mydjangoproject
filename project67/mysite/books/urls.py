from django.urls import path
from .views import book_list, book_detail, search_books

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
    path('search/', search_books, name='search'),
]