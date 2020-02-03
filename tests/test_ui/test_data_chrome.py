#!/usr/bin/python3
""" Test cases for data page using Selenium and Chrome """

import unittest
from selenium import webdriver


class TestDataChrome(unittest.TestCase):
    """class TestDataChrome"""

    @classmethod
    def setUpClass(cls):
        """Setup class"""
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    def test_summary_data(self):
        """Go to find out more on summary section"""
        self.driver.get('http://psl-outbreak.herokuapp.com')
        self.driver.find_element_by_id('summary_find_out').click()

    def test_summary_report(self):
        """Go to report cases on summary section"""
        self.driver.get('http://psl-outbreak.herokuapp.com')
        self.driver.find_element_by_id('summary_report_cases').click()

    @classmethod
    def tearDownClass(cls):
        """Teardown for closing the session when tests are done"""
        cls.driver.close()
        cls.driver.quit()
