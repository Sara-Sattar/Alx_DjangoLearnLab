from relationship_app.models import Author, Book, Library, Librarian

def sample_data():
    author = Author.objects.create(name="George Orwell")
    book1 = Book.objects.create(title="1984", author=author)
    book2 = Book.objects.create(title="Animal Farm", author=author)

    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2)

    Librarian.objects.create(name="Alice", library=library)

def queries():
    author_name = "George Orwell"
    author = Author.objects.get(name=author_name)
    print(author.books.all())

    library_name = "Central Library"
    library = Library.objects.get(name=library_name)
    print(library.books.all())

    library = Library.objects.get(name=library_name)
    print(library.librarian)
