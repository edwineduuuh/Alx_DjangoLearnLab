```python
retrieved = Book.objects.get()  
>>> print(retrieved.title)
1984
>>> print(retrieved.author) 
George Orwell
>>> print(retrieved.publication_year) 
1949