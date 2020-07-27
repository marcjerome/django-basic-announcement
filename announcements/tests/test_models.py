from django.test import TestCase
from datetime import date
from announcements.models import Announcement

class AnnouncementModelTest(TestCase):

    def test_default_text(self):
        announcement = Announcement()
        self.assertEqual(announcement.text, '')
    
    def test_string_representation(self):
        announcement = Announcement(text='Website down')
        self.assertEqual(str(announcement), 'Website down')

    def test_default_date(self):
        announcement = Announcement()
        announcement.save()
        self.assertEqual(announcement.date, date.today())