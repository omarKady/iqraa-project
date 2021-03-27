from django.test import TestCase
from django.urls import reverse
from .models import Article
# Create your tests here.

class HomePageViewTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        template_name = 'home.html'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    

class ListArticlesPageViewTests(TestCase):
    def setUp(self):
        Article.objects.create(title='New Article for test')        

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('list_all_articles'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/all_articles/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/all_articles/')
        template_name = 'list_all_articles.html'
        self.assertTemplateUsed(response, template_name)

    def test_list_article_view_content(self):
        response = self.client.get(reverse('list_all_articles'))
        self.assertContains(response, 'New Article for test')
        no_response = self.client.get('article/1000/')
        self.assertEqual(no_response.status_code, 404)

class ArticleModelTests(TestCase):

    def setUp(self):
        Article.objects.create(title="Test Article")
    
    def test_article_text_content(self):
        article = Article.objects.get(id=1)
        expected_article_name = f'{article.title}'
        self.assertEqual(expected_article_name, "Test Article")
        