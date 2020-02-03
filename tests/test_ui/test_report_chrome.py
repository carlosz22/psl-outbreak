#!/usr/bin/python3
""" Test cases for report page using Selenium and Chrome """

import unittest
from selenium import webdriver


class TestReportChrome(unittest.TestCase):
    """class TestReportChrome"""

    @classmethod
    def setUpClass(cls):
        """Setup class"""
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    def test_send_correct_data(self):
        """Go to find out more on summary section"""
        self.driver.get('http://psl-outbreak.herokuapp.com/report')
        self.driver.find_element_by_xpath("//select[@name='state_id']/option[text()='Casanare']").click()
        self.driver.find_element_by_name('number_infections').send_keys("100")
        self.driver.find_element_by_id('submit').click()

    def test_send_inaccurate_data(self):
        """Go to report cases on summary section"""
        self.driver.get('http://psl-outbreak.herokuapp.com/report')
        self.driver.find_element_by_xpath("//select[@name='state_id']/option[text()='Casanare']").click()
        self.driver.find_element_by_name('number_infections').send_keys("100")
        self.driver.find_element_by_id('submit').click()

    @classmethod
    def tearDownClass(cls):
        """Teardown for closing the session when tests are done"""
        cls.driver.close()
        cls.driver.quit()
