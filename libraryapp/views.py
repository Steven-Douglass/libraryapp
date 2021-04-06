from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Book, Author, Member, Library

def index(request):
    book_list = Book.objects.order_by('id')
    context = { 'book_list': book_list }
    return render(request, 'libraryapp/index.html', context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'libraryapp/authordetail.html', {'author': author})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'libraryapp/bookdetail.html', {'book': book})

def library_detail(request, library_id):
    library = get_object_or_404(Library, pk=library_id)
    return render(request, 'libraryapp/librarydetail.html', {'library': library})
    
def member_detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'libraryapp/memberdetail.html', {'member': member})