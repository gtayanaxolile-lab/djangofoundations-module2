from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

def home(request):
    return render(request, 'core/home.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'core/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'core/book_detail.html', {'book': book})

def book_create(request):
    from .forms import BookForm
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'core/book_form.html', {'form': form})

def book_update(request, pk):
    from .forms import BookForm
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm(instance=book)
    return render(request, 'core/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'core/book_confirm_delete.html', {'book': book})
