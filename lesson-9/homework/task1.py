class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

class Member:
    MAX_BORROWED_BOOKS = 3
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= Member.MAX_BORROWED_BOOKS:
            raise MemberLimitExceededException(f"{self.name} has reached the borrowing limit.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")
        
        book.is_borrowed = True
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed {book.title}.")
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}.")
        else:
            print(f"{self.name} does not have {book.title}.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_member(self, member):
        self.members.append(member)
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library.")
    def borrow_book(self, member_name, book_title):
        member = None
        for m in self.members:
            if m.name == member_name:
                member = m
                break
        
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        
        try:
            book = self.find_book(book_title)
            member.borrow_book(book)
        except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
            print(e)
    
    def return_book(self, member_name, book_title):
        member = None
        for m in self.members:
            if m.name == member_name:
                member = m
                break
        
        if not member:
            print(f"Member '{member_name}' not found.")
            return
        
        try:
            book = self.find_book(book_title)
            member.return_book(book)
        except BookNotFoundException as e:
            print(e)