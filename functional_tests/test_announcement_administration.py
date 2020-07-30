from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time 

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
        announcement_inputbox = self.wait_for_element_by_id('id_text')
        announcement_inputbox.send_keys('We will have a website maintainance tomorrow')
        announcement_inputbox.send_keys(Keys.ENTER)
                
        # After saving, he saw his announcement in the website 
        element = self.wait_for_element('announcement_text')
        self.assertEqual(element.text, 'We will have a website maintainance tomorrow')

        # He deletes it because the event that was announced was cancelled
        delete_latest_announcement = self.browser.find_element_by_class_name('deleteButton')
        delete_latest_announcement.click()

        with self.assertRaises(NoSuchElementException):
            element = self.wait_for_element('announcement_text')

        # After a while, he posts another announcement. This time it's confirmed it's gonna happen
        announcement_inputbox = self.wait_for_element_by_id('id_text')
        announcement_inputbox.send_keys('NCov-19 Update: The business operations of the company will be limited until a vaccine is found')
        announcement_inputbox.send_keys(Keys.ENTER)
                
        # He then realizes that there's an established name for the virus already so he updates it
        update_latest_announcement = self.wait_for_element('updateButton')
        update_latest_announcement.click()

        # The site redirected him to an update page filled up with the data from the previous page
        announcement_inputbox = self.wait_for_element_by_id('id_text')
        print(announcement_inputbox.text)
        self.assertEqual(announcement_inputbox.get_attribute('value'),'NCov-19 Update: The business operations of the company will be limited until a vaccine is found')

        # He clears the input box and updates the announcement
        announcement_inputbox.clear()
        announcement_inputbox.send_keys('Covid-19 Update: The business operations of the company will be limited until a vaccine is found')
        announcement_inputbox.send_keys(Keys.ENTER)

        # Finally, he sees his announcement correct in the announcement home page
        element = self.wait_for_element('announcement_text')
        self.assertEqual(element.text, 'Covid-19 Update: The business operations of the company will be limited until a vaccine is found')
