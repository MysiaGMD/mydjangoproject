
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from books.models import Author, Books, BookDetail


BookDetail.objects.all().delete()
Books.objects.all().delete()
Author.objects.all().delete()


authors = [
    Author(name='лев толстой', img_src='', years_of_age='1828-1910',
           bio='Русский писатель, философ, публицист, родоначальник толстовства.',
           works='Война и мир, Анна Каренина'),

    Author(name='фёдор достоевский', img_src='', years_of_age='1821-1881',
           bio='Один из величайших русских писателей, мыслитель, философ.',
           works='Преступление и наказание, Идиот'),

    Author(name='александр пушкин', img_src='', years_of_age='1799-1837',
           bio='Русский поэт, драматург, основоположник современного русского языка.',
           works='Евгений Онегин, Борис Годунов'),

    Author(name='джордж оруэлл', img_src='', years_of_age='1903-1950',
           bio='Британский писатель и публицист, автор антиутопий.',
           works='1984, Скотный двор'),

    Author(name='фрэнсис скотт фицджеральд', img_src='', years_of_age='1896-1940',
           bio='Американский писатель, мастер прозы.',
           works='Великий Гэтсби, Ночь нежна')
]

Author.objects.bulk_create(authors)


books = [
    Books(
        title='война и мир', 
        author_name='лев толстой', 
        price=5000
     ),
    Books(
        title='преступление и наказание', 
        author_name='фёдор достоевский', 
        price=4500
     ),
    Books(
        title='евгений онегин', 
        author_name='александр пушкин', 
        price=3000
     ),
    Books(
        title='1984', 
        author_name='джордж оруэлл', 
        price=4000
     ),
    Books(
        title='великий гэтсби', 
        author_name='фрэнсис скотт фицджеральд', 
        price=3500
     )
]

Books.objects.bulk_create(books)



book_details = [
    BookDetail(
        isbn='978-5-17-090123-4',
        pages=1300,
        publisher='АСТ'
    ),
    BookDetail(
        isbn='978-5-17-090456-7',
        pages=672,
        publisher='АСТ'
    ),
    BookDetail(
        isbn='978-5-17-090789-0',
        pages=352,
        publisher='Эксмо'
    ),
    BookDetail(
        isbn='978-5-17-091234-5',
        pages=320,
        publisher='АСТ'
    ),
    BookDetail(
        isbn='978-5-17-091567-8',
        pages=256,
        publisher='Эксмо'
    )
]

BookDetail.objects.bulk_create(book_details)

print('База данных успешно обновлена!')
print('Добавлено авторов:', Author.objects.count())
print('Добавлено книг:', Books.objects.count())
print('Добавлено подробностей:', BookDetail.objects.count())