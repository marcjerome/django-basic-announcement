from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class AnnouncerTest(FunctionalTest):


    def test_admin_can_create_annoucement(self):
        
        # The admin of a website wants to annouce something to the users of the website 
        # He logged in first
        
        self.browser.get(self.live_server_url)
        username = self.browser.find_element_by_id('id_username')
        username.send_keys('admin')

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('password123')
        password.send_keys(Keys.ENTER)

        # He is redirected to the announcement admin page
        page_heading = self.browser.find_element_by_id('head')
        self.assertEqual(page_heading, 'Announcement admin')

    