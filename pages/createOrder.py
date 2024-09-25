from selenium import webdriver
import time
import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locators():

    # create new order
    createNewOrderBox = '//*[@id="root"]/div/div[2]/div[1]/div/button[1]'

    # header
    createDeliveryTitle = '//*[@id="chakra-modal--header-:rh:"]'

    # select customer
    selectCustomer = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[1]/div/div/select'
    nextButton = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[1]/button'

    # select customer branch
    customerBranch = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[2]/div[1]/div/select'
    location = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[2]/div[2]/div/select'
    nextButtonB = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[2]/button[2]'

    # delivery details
    bulkDelivery = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[2]/div[1]/div/select'
    checkBox = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/label/span[1]'
    quantity = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/input'

    selectDriver = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[3]/div[1]/div/div/select'
    assetCategory = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[3]/div[2]/div/div/select'

    # recurring delivery
    enableRecurringDelivery = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[2]/div[2]/label/span'
    createOrderButton = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/button[2]'

    startDateCalendar = '//*[@id="tabs-:r12:--tabpanel-2"]/button[2]'
    selectFrequency = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[2]/div[2]/div[2]/div/select'
    endDateCalendar = '/html/body/div[3]/div[3]/div/section/div/div/div/div/div[2]/div[3]/div[2]/div[2]/div[3]/input'

class CreateOrderPage():

    def __init__(self, driver):
        self.driver = driver
        self.createDeliveryTitle = Locators.createDeliveryTitle
        self.createNewOrderBox = Locators.createNewOrderBox
        self.selectCustomer = Locators.selectCustomer
        self.nextButton = Locators.nextButton
        self.customerBranch = Locators.customerBranch
        self.location = Locators.location
        self.nextButtonB = Locators.nextButtonB
        self.bulkDelivery = Locators.bulkDelivery
        self.checkBox = Locators.checkBox
        self.quantity = Locators.quantity
        self.selectDriver = Locators.selectDriver
        self.assetCategory = Locators.assetCategory
        self.enableRecurringDelivery = Locators.enableRecurringDelivery
        self.createOrderButton = Locators.createOrderButton
        self.startDateCalendar = Locators.startDateCalendar
        self.selectFrequency = Locators.selectFrequency
        self.endDateCalendar = Locators.endDateCalendar


    def clickCreateBox(self):
        self.driver.find_element(By.XPATH, self.createNewOrderBox).click()
        time.sleep(3)

    def verifyTitle(self):
        # self.driver.window_handles()
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="chakra-modal-:rh:"]')))

        # self.driver.switch_to.alert
        print("function called")
        self.driver.implicitly_wait(10)
        # print("hmmm")
        self.title = self.driver.find_element(By.XPATH, self.createDeliveryTitle).text
        print(f"Title of the element: {self.title}")
        assert "create" in self.title.lower()
        print("yess verified")

    def clickCustomerBox(self, customerName):
        self.selectName = self.driver.find_element(By.XPATH, self.selectCustomer)
        select = Select(self.selectName)
        select.select_by_value(customerName)
        time.sleep(1)

    def clickNext(self):
        self.driver.find_element(By.XPATH, self.nextButton).click()
        time.sleep(2)

    def clickBranchBox(self, branchName):
        # self.driver.implicitly_wait(10)
        # self.branch = self.driver.find_element(By.XPATH, self.customerBranch)
        # select = Select(self.branch)
        # select.select_by_value(branchName)
        Select(self.driver.find_element(By.XPATH, self.customerBranch)).select_by_value(branchName)
        time.sleep(1)

    def selectLocation(self, location):
        Select(self.driver.find_element(By.XPATH, self.location)).select_by_value(location)
        time.sleep(1)

    def clickNextButton(self):
        self.driver.find_element(By.XPATH, self.nextButtonB).click()
        time.sleep(1)

    def clickBulkDelivery(self, product):
        Select(self.driver.find_element(By.XPATH, self.bulkDelivery)).select_by_visible_text(product)
        time.sleep(2)

    def clickCheckbox(self):

        self.driver.find_element(By.XPATH, self.checkBox).click()
        time.sleep(2)

    def inputQuantity(self, sendQuantity):
        self.driver.find_element(By.XPATH, self.quantity).send_keys(sendQuantity)
        time.sleep(1)

    def clickSelectDriver(self, driver):
        Select(self.driver.find_element(By.XPATH, self.selectDriver)).select_by_value(driver)
        time.sleep(1)

    def clickAssetCategory(self, category):
        Select(self.driver.find_element(By.XPATH, self.assetCategory)).select_by_value(category)
        time.sleep(1)

    def enableReccuring(self):
        self.driver.find_element(By.XPATH, self.enableRecurringDelivery).click()
        time.sleep(2)

    def clickFrequency(self, frequency):
        Select(self.driver.find_element(By.XPATH, self.selectFrequency)).select_by_value(frequency)
        time.sleep(1)

    def clickRecuringEndDate(self, endDate):
        self.driver.find_element(By.XPATH, self.endDateCalendar).send_keys(endDate)
        time.sleep(2)

    def clickCreateOrder(self):
        self.driver.find_element(By.XPATH, self.createOrderButton).click()
        # time.sleep(10)

    def verifySuccess(self):

        # verify toast message
        try:
            # Wait for the toast message to appear with explicit wait
            self.driver.implicitly_wait(10)
            # self.toast_message_element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, ".//*[contains(@text, 'Order')]"))
            # )

            self.toast_message_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]").text
            # Get the text from the toast message
            # self.toast_message_text = self.toast_message_element.text
            print(f"to verify: {self.toast_message_element}")
            # Verify that the toast message contains the word "Order Created"
            assert "order created" in self.toast_message_element.lower()
            print("Toast message verified, new order created successfully!")

        except Exception as e:
            print(f"Failed to verify toast message: {str(e)}")