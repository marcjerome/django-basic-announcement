from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from announcements.models import Announcement
from announcements.forms import AnnouncementForm

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

    def test_announcement_form_in_view(self):
        self.client.login(username='admin', password='pass@123')
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], AnnouncementForm)
    
    def test_redirects_to_home_if_unauthenticated(self):
        response = self.client.post(f'/announcement/delete/0/')
        self.assertEqual(response.status_code, 302)
    

class AnnouncementAddViewTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='admin', password='pass@123', email='admin@admin.com')
        self.client = Client()
    
    def test_redirects_to_home_if_unauthenticated(self):
        response = self.client.post(f'/announcement/delete/0/')
        self.assertEqual(response.status_code, 302) 

    def test_can_save_post_request(self):
        self.client.login(username='admin', password='pass@123')
        self.client.post('/announcement/add/', data={'text': 'Website down'})
        self.assertEqual(Announcement.objects.count(), 1)
        new_announcement = Announcement.objects.first()
        self.assertEqual(new_announcement.text, 'Website down')

class AnnouncementDeleteViewTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='admin', password='pass@123', email='admin@admin.com')
        self.client = Client()

    def test_can_delete_added_announcement(self):
        self.client.login(username='admin', password='pass@123')
        
        new_announcement = Announcement()
        new_announcement.save()
        self.client.post(f'/announcement/delete/{new_announcement.id}/')
        self.assertEqual(Announcement.objects.count(), 0)
    
    def test_redirects_to_home_if_unauthenticated(self):
        response = self.client.post(f'/announcement/delete/0/')
        self.assertEqual(response.status_code, 302)
    
class AnnouncementUpdateViewTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='admin', password='pass@123', email='admin@admin.com')
        self.client = Client()
    
    def test_can_update_announcement(self):
        self.client.login(username='admin', password='pass@123')
                
        new_announcement = Announcement()
        new_announcement.save()

        self.client.post(f'/announcement/update/{new_announcement.id}/', data={'text': 'Website down'})
        updated_announcement = Announcement.objects.get(id=new_announcement.id)
        self.assertEqual(updated_announcement.text, 'Website down')
    
    def test_redirects_to_home_if_unauthenticated(self):
        response = self.client.post(f'/announcement/update/0/')
        self.assertEqual(response.status_code, 302)
    
    def test_update_view_uses_correct_form(self):
        self.client.login(username='admin', password='pass@123')

        new_announcement = Announcement()
        new_announcement.save()

        response = self.client.get(f'/announcement/update/{new_announcement.id}/')
        self.assertIsInstance(response.context['form'], AnnouncementForm)
    
    def test_update_uses_proper_template(self):
        self.client.login(username='admin', password='pass@123')
        
        new_announcement = Announcement()
        new_announcement.save()

        response = self.client.get(f'/announcement/update/{new_announcement.id}/')
        self.assertTemplateUsed(response, 'update.html')