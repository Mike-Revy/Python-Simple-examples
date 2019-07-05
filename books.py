class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return '{} by {}'.format(self.title, self.author)
	
class Bookcase: 
    def __init__(self, books=None):
        self.books = books
        
    @classmethod
    def create_bookcase(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title,author))
        return cls(books)
            
            
#>>> from books import Book, Bookcase
#>>> bc = Bookcase.create_bookcase([('Moby-Dick', 'Herman Melville'), #('Jungle Book', 'Rudyard Kipling')])
#>>> bc.books
#[<books.Book object at 0x000001F3ADC675F8>, <books.Book object at #0x000001F3ADDA0400>]
#>>> bc
#<books.Bookcase object at 0x000001F3ADC67588>
#>>> bc.books[0]
#<books.Book object at 0x000001F3ADC675F8>
#>>> bc.books[0].author
#'Herman Melville'
#>>> bc.books[0].title
#'Moby-Dick'
#>>> str(bc.books[0])
#'Moby-Dick by Herman Melville'