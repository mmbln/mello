# functionaltests/tests.py 
# -*- coding: utf-8 -*-

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HomePageTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('title').text
        self.assertIn('Mello', page_text)

    def test_project_list(self):
        self.browser.get('%s%s' % (self.live_server_url, '/project/'))
        page_text = self.browser.find_element_by_tag_name('title').text
        self.assertIn('Hallo', page_text)


    
