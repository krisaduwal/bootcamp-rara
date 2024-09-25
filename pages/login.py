from selenium import webdriver
import time
import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locators():

    # login elements
    emailBox = '//*[@id="email"]'
    passwordBox = '//*[@id="password"]'
    visibleElement = '/html/body/div[1]/div/div/form/div/div[2]/div/div/button'
    loginButtonBox = '/html/body/div[1]/div/div/form/div/button'
    forgetPW = '/html/body/div[1]/div/div/div/a'
    invalidCreds = '//*[@id="root"]/div/div/p'
    dashboardEl = '//*[@id="root"]/div/div[1]/div/a/div'
    darkmode = '//*[@id="root"]/div/div[1]/div/button'



class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.emailBox = Locators.emailBox
        self.passwordBox = Locators.passwordBox
        self.visibleElement = Locators.visibleElement
        self.loginButtonBox = Locators.loginButtonBox
        self.dashboardEl = Locators.dashboardEl
        self.darkmode = Locators.darkmode

        self.invalidCreds = Locators.invalidCreds

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.emailBox).send_keys(email)
        time.sleep(2)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.passwordBox).send_keys(password)
        time.sleep(1)

    def checkPw(self):
        self.driver.find_element(By.XPATH, self.visibleElement).click()
        time.sleep(1)

    def clickLogIn(self):
        self.driver.find_element(By.XPATH, self.loginButtonBox).click()
        time.sleep(1)

    def verifyDashboard(self):
        try:

            print("hello")
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.dashboardEl))
            )
            print("element found")
            title = element.text
            print(f"Element text: {title}")
            assert "dashboard" in title.lower()
            print("logged in successfully")
            time.sleep(2)
            # print("success")

        except TimeoutException:
            print("Element not found within the given time.")
        except AssertionError:
            print(f"Assertion failed. Expected 'dashboard', but got '{title}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def setDarkmode(self):
        self.driver.find_element(By.XPATH, self.darkmode).click()
        time.sleep(1)
    def enter_invalidEmail(self, Inemail):
        self.driver.find_element(By.XPATH, self.emailBox).send_keys(Inemail)
        time.sleep(1)

    def enter_invalidPassword(self, Inpassword):
        self.driver.find_element(By.XPATH, self.passwordBox).send_keys(Inpassword)
        time.sleep(2)

    def verify_invalid(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.invalidCreds))
            )
            title = element.text
            print(f"element text: {title}")
            assert "invalid email or password" in title.lower()
            print("incorrect credentials")

        except TimeoutException:
            print("Element not found within the given time.")
        except AssertionError:
            print(f"Assertion failed. Expected 'invalid email or password', but got '{title}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")