from django.test import TestCase, Client
from django.contrib.auth import get_user_model

class HomeViewTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='admin', password='pass@123', email='admin@admin.com')
        self.client = Client()

    def test_home_redirect_to_login_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)


    def test_home_uses_proper_template(self):
        self.client.login(username='admin', password='pass@123')
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_status_code(self):
        self.client.login(username='admin', password='pass@123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

