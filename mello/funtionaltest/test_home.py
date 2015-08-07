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

    # Project
    
    def test_home_page(self):
        self.browser.get(self.live_server_url)
        page_text = self.browser.page_source
        self.assertIn('Projekte', page_text)

    def test_project_list(self):
        self.browser.get('%s%s' % (self.live_server_url, '/project/'))
        page_text = self.browser.page_source
        self.assertIn('Projekte', page_text)

    def test_new_project_test_page(self):
        self.browser.get('%s%s' % (self.live_server_url, '/project/new/'))
        page_text = self.browser.page_source
        self.assertIn('Neues Projekt', page_text)

    # Member
        
    def test_member_list(self):
        self.browser.get('%s%s' % (self.live_server_url, '/member/'))
        page_text = self.browser.page_source
        self.assertIn('Mitglieder', page_text)

    def test_new_member_test_page(self):
        self.browser.get('%s%s' % (self.live_server_url, '/member/new/'))
        page_text = self.browser.page_source
        self.assertIn('Neues Mitglied', page_text)

    def test_add_member(self):
        self.assertIn('a', 'a')     



    
