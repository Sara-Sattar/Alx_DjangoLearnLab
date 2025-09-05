from relationship_app.models import Author, Book, Library, Librarian

def sample_data():
    author = Author.objects.create(name="George Orwell")
    
    book1 = Book.objects.create(title="1984", author=author)
    book2 = Book.objects.create(title="Animal Farm", author=author)
    
    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2)
    
    librarian = Librarian.objects.create(name="Alice", library=library)

def queries():
    orwell = Author.objects.get(name="George Orwell")
    print(orwell.books.all())  

    central = Library.objects.get(name="Central Library")
    print(central.books.all())

    print(central.librarian)
