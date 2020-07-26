from django.test import TestCase
from datetime import datetime

class AnnouncementModelTest(TestCase):

    def test_default_text(self):
        announcement = Announcement()
        self.assertEqual(announcement.text, '')
    
    def test_string_representation(self):
        announcement = Announcement(text='Website down')
        self.assertEqual(str(announcement), 'Website down')

    def test_default_date(self):
        announcement = Announcement()
        self.assertEqual(announcement.date, datetime.now())