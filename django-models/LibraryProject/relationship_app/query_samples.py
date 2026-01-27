"""
Sample queries demonstrating Django ORM relationships.

This script contains query examples for:
1. ForeignKey relationship (Book -> Author)
2. ManyToManyField relationship (Library <-> Book)
3. OneToOneField relationship (Librarian <-> Library)

Usage:
    python manage.py shell < relationship_app/query_samples.py
    
Or in Django shell:
    from relationship_app.query_samples import *
"""

import os
import sys
import django

# Setup Django environment (only needed if running as standalone script)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# Add the parent directory to the path so Django can find the project
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    Demonstrates ForeignKey relationship traversal.
    
    Args:
        author_name (str): Name of the author to search for
        
    Returns:
        QuerySet: All books by the specified author
    """
    try:
        # Get author object
        author = Author.objects.get(name=author_name)
        # Query all books by this author using filter
        books = Book.objects.filter(author=author)
        
        print(f"\n{'='*60}")
        print(f"Books by {author_name}:")
        print(f"{'='*60}")
        
        if books.exists():
            for book in books:
                print(f"  - {book.title}")
        else:
            print(f"  No books found for author: {author_name}")
            
        return books
        
    except Author.DoesNotExist:
        print(f"\nAuthor '{author_name}' not found in database.")
        return Book.objects.none()


def list_books_in_library(library_name):
    """
    List all books in a specific library.
    Demonstrates ManyToManyField relationship traversal.
    
    Args:
        library_name (str): Name of the library
        
    Returns:
        QuerySet: All books in the specified library
    """
    try:
        # Get library and access related books through ManyToMany field
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        
        print(f"\n{'='*60}")
        print(f"Books in {library_name}:")
        print(f"{'='*60}")
        
        if books.exists():
            for book in books:
                print(f"  - {book.title} by {book.author.name}")
        else:
            print(f"  No books found in library: {library_name}")
            
        return books
        
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found in database.")
        return Book.objects.none()


def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a specific library.
    Demonstrates OneToOneField relationship traversal.
    
    Args:
        library_name (str): Name of the library
        
    Returns:
        Librarian or None: The librarian for the specified library
    """
    try:
        # Get library and access related librarian through OneToOne field
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        
        print(f"\n{'='*60}")
        print(f"Librarian for {library_name}:")
        print(f"{'='*60}")
        print(f"  {librarian.name}")
        
        return librarian
        
    except Library.DoesNotExist:
        print(f"\nLibrary '{library_name}' not found in database.")
        return None
    except Librarian.DoesNotExist:
        print(f"\nNo librarian assigned to library: {library_name}")
        return None


def create_sample_data():
    """
    Create sample data for testing the queries.
    """
    print("\n" + "="*60)
    print("Creating Sample Data...")
    print("="*60)
    
    # Create Authors
    author1, created = Author.objects.get_or_create(name="J.K. Rowling")
    author2, created = Author.objects.get_or_create(name="George Orwell")
    author3, created = Author.objects.get_or_create(name="Jane Austen")
    
    # Create Books
    book1, created = Book.objects.get_or_create(
        title="Harry Potter and the Philosopher's Stone",
        defaults={'author': author1}
    )
    book2, created = Book.objects.get_or_create(
        title="Harry Potter and the Chamber of Secrets",
        defaults={'author': author1}
    )
    book3, created = Book.objects.get_or_create(
        title="1984",
        defaults={'author': author2}
    )
    book4, created = Book.objects.get_or_create(
        title="Animal Farm",
        defaults={'author': author2}
    )
    book5, created = Book.objects.get_or_create(
        title="Pride and Prejudice",
        defaults={'author': author3}
    )
    
    # Create Libraries
    library1, created = Library.objects.get_or_create(name="Central Library")
    library2, created = Library.objects.get_or_create(name="City Library")
    
    # Add books to libraries
    library1.books.add(book1, book2, book3)
    library2.books.add(book3, book4, book5)
    
    # Create Librarians
    librarian1, created = Librarian.objects.get_or_create(
        library=library1,
        defaults={'name': 'Alice Johnson'}
    )
    librarian2, created = Librarian.objects.get_or_create(
        library=library2,
        defaults={'name': 'Bob Smith'}
    )
    
    print("Sample data created successfully!")
    print(f"  - {Author.objects.count()} authors")
    print(f"  - {Book.objects.count()} books")
    print(f"  - {Library.objects.count()} libraries")
    print(f"  - {Librarian.objects.count()} librarians")


def run_all_queries():
    """
    Run all sample queries with the created data.
    """
    print("\n" + "#"*60)
    print("# RUNNING ALL SAMPLE QUERIES")
    print("#"*60)
    
    # Query 1: Books by a specific author (ForeignKey)
    query_books_by_author("J.K. Rowling")
    query_books_by_author("George Orwell")
    
    # Query 2: Books in a library (ManyToMany)
    list_books_in_library("Central Library")
    list_books_in_library("City Library")
    
    # Query 3: Librarian for a library (OneToOne)
    retrieve_librarian_for_library("Central Library")
    retrieve_librarian_for_library("City Library")
    
    print("\n" + "="*60)
    print("All queries completed!")
    print("="*60 + "\n")


# Main execution block
if __name__ == "__main__":
    print("\n" + "#"*60)
    print("# Django ORM Relationship Queries Demo")
    print("#"*60)
    
    # Check if sample data exists
    if Author.objects.count() == 0:
        print("\nNo data found. Creating sample data...")
        create_sample_data()
    else:
        print(f"\nFound existing data:")
        print(f"  - {Author.objects.count()} authors")
        print(f"  - {Book.objects.count()} books")
        print(f"  - {Library.objects.count()} libraries")
        print(f"  - {Librarian.objects.count()} librarians")
    
    run_all_queries()