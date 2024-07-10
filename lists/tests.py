from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


# Create your tests here.
class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        # request = HttpRequest()
        # response = home_page(request)
        # html = response.content.decode('utf8')
        # self.assertTrue(html.startswith('<html lang="en">'))
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.strip().endswith('</html>'))

        # expected_html = render_to_string('home.html')
        # self.assertEqual(html, expected_html)

        # django风格的测试语句
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'home.html')
