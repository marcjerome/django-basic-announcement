from django.db import models

class Announcement(models.Model):
    text = models.CharField(default='', max_length=500, help_text='What are you going to announce?')
    date = models.DateField(auto_now=True, help_text='Date when announcement was created')

    def __str__(self):
        return self.text

    class Meta:
        unique_together = ['text', 'date']