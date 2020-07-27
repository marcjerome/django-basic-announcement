from django.test import TestCase
from announcements.forms import AnnouncementForm
from announcements.models import Announcement

class AnnouncementFormTest(TestCase):

    def test_form_save(self):
        form = AnnouncementForm(data={'text': 'Website Down'})
        new_announcement = form.save()
        self.assertEqual(new_announcement, Announcement.objects.all()[0])