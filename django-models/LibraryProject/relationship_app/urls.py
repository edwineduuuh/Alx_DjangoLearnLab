from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    #Function based view url pattern
    path('books/', views.list_books, name = 'list_books'),

    #class based view url pattern
    path('library/<int:pk>/', LibraryDetailView.as_view(), name = 'library_detail'),
]