from django.test import TestCase
from django.urls import reverse
from . import views
from .models import Book, Comments
# Create your tests here.


class ReadBookViewTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/books/read/')
        self.assertEqual(response.status_code, 200)

    def test_view_by_view_name(self):
        response = self.client.get(reverse(views.read_book_view))
        self.assertEqual(response.status_code, 200)
    
    def test_view_by_named_url(self):
        response = self.client.get(reverse('read_books'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get('/books/read/')
        template_name = 'read_books.html'
        self.assertTemplateUsed(resp, template_name)

class BookDetailViewTest(TestCase):
    
    def setUp(self):
        Book.objects.create(name='Test Book')

    def test_book_object_content(self):
        book = Book.objects.get(id=1)
        expected_book_name = f'{book.name}'
        self.assertEqual(expected_book_name, "Test Book")
    
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/books/book_detail/1')
        self.assertEqual(response.status_code, 200)
    
    def test_string_representation(self):
        book = Book(name='First Book')
        self.assertEqual(str(book), 'First Book')

class AddCommentViewTest(TestCase):

    def setUp(self):
        book = Book.objects.create(name='Test Book')
        Comments.objects.create(text="Test Comment", related_book=book)
    
    def test_comment_object_content(self):
        comment = Comments.objects.get(id=1)
        comment_text = f'{comment.text}'
        self.assertEqual(comment_text, "Test Comment")