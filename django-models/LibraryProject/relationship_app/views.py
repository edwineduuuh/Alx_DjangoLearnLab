from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
# Create your views here.
def list_books(request):
    """
    Function based view that lists all books in the database.
    Displays book titles and their authors
    Args: 
        request: HttpRequest object
    Returns:
        HttpResponse with rendered template showing all books
    """
    
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    """
    Class based view that displays details for a specific library
    Shows all books available in that library
    """
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    