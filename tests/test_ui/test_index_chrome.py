#!/usr/bin/python3
""" Test cases for index page using Selenium and Chrome """

import unittest
from selenium import webdriver


class TestIndexChrome(unittest.TestCase):
    """class TestIndexChrome"""

    @classmethod
    def setUpClass(cls):
        """Setup class"""
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    def test_summary_data(self):
        """Go to find out more on summary section"""
        self.driver.get('http://psl-outbreak.herokuapp.com/report')
        self.driver.find_element_by_id('summary_find_out').click()

    def test_summary_report(self):
        """Go to report cases on summary section"""
        self.driver.get('http://psl-outbreak.herokuapp.com/report')
        self.driver.find_element_by_id('summary_report_cases').click()

    @classmethod
    def tearDownClass(cls):
        """Teardown for closing the session when tests are done"""
        cls.driver.close()
        cls.driver.quit()
