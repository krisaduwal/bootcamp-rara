from selenium import webdriver
import time
import unittest
import os
import sys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages.login import LoginPage
from pages.createOrder import CreateOrderPage
service = Service("C:\\Users\\acer\\AppData\\Roaming\\Python\\Python312\\chromedriver-win64\\chromedriver.exe")
class LogIn(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        # cls.driver.get("http://localhost:5173/")


    def test_logIn(self):
        driver = self.driver
        driver.get("http://localhost:5173/")
        login = LoginPage(driver)
        login.enter_email('krisha.duwal@fleetpanda.com')
        login.enter_password('Test@123')
        login.checkPw()
        login.clickLogIn()
        login.verifyDashboard()
        login.setDarkmode()

    def test_notvalid_creds(self):
        # self.test_logIn()
        driver = self.driver
        driver.get("http://localhost:5173/")
        invalidLogin = LoginPage(driver)
        invalidLogin.enter_invalidEmail('k@d.com')
        invalidLogin.enter_invalidPassword('985434567')
        invalidLogin.checkPw()
        invalidLogin.clickLogIn()
        invalidLogin.verify_invalid()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
