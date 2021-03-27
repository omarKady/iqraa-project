from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Comments
from .forms import CommentBookForm

# Create your views here.

def read_book_view(request):
    all_books = Book.objects.all()
    return render(request, 'read_books.html', {'all_books': all_books})

def book_detail_view(request, pk):
    book_data = Book.objects.get(pk=pk)
    return render(request, 'book_details.html', {'book_data': book_data})

def comment_book_view(request, pk):
    template_name = 'comment_book.html'
    book = get_object_or_404(Book, pk=pk)
    # print("Book id: ", book.id)
    if request.method == "POST":
        comment_form = CommentBookForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.related_book = book
            comment.comment_author = request.user.username
            comment.save()
            return redirect(Comments.get_absolute_url(comment))
    else:
        name = request.user.username
        comment_form = CommentBookForm(initial={'comment_author':name, 'related_book':book})
    return render(request, template_name, {'form':comment_form})