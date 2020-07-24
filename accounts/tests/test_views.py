from django.test import TestCase

class LoginPageTest(TestCase):

    def test_status_code_loginpage(self):
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 301)

    def test_loginpage_has_proper_template(self):
        response = self.client.get('/accounts/login/')
        self.assertTemplateUsed(response, 'registration/login.html')

    
