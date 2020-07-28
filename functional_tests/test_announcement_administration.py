from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class AnnouncerTest(FunctionalTest):


    def test_announcement_crud_administration(self):
        
        # The admin of a website wants to annouce something to the users of the website 
        # He logged in first
        
        self.browser.get(self.live_server_url)
        username = self.browser.find_element_by_id('id_username')
        username.send_keys('test')

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('tset123')
        password.send_keys(Keys.ENTER)

        # He is redirected to the announcement admin page
        element = self.wait_for_element('head')
        self.assertEqual(element.text, 'Announcement admin')

        # He wants to announce that there will be site maintainance  so he 
        # filled up the form and announce it
        announcement_inputbox = self.browser.find_element_by_id('id_text')
        announcement_inputbox.send_keys('We will have a website maintainance tomorrow')
        announcement_inputbox.send_keys(Keys.ENTER)
                
        # After saving, he saw his announcement in the website 
        element = self.wait_for_element('announcement_text')
        self.assertEqual(element.text, 'We will have a website maintainance tomorrow')

        delete_latest_announcement = self.browser.find_element_by_class_name('deleteButton')[0]
        delete_latest_announcement.click()

        element = self.browser.find_element_by_class_name('announcement_text')
        self.assertFalse(element.is_displayed())
