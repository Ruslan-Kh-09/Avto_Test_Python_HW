from book import Book

library = [
    Book('Мастер и Маргарита', 'Михаил Булгаков'),
    Book('Три товарища', 'Ремарк'),
    Book('Анна Каренина', 'Лев Толстой')
]

print('Моя библиотека:')
for book in library:
    print(f'{book.book_title} - {book.autor}')