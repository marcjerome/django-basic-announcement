from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):

    def  wait_for_element(self, text_location):
        start_time = time.time()
        while True:
            try:
                element = self.browser.find_element_by_class_name(text_location)
                return element
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

     

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.user = User.objects.create_superuser(username='test', password='tset123', email='test@test.com', is_active=True, is_staff=True)
        self.user.save()

    def tearDown(self):
        self.browser.quit()