import time

from pages.createOrder import *

class Locators():

    productsButton = '/html/body/div[1]/div/div[1]/div/nav/a[2]'
    productListTitle = '/html/body/div[1]/div/div[2]/div[1]/h2'
    createProductBox = '/html/body/div[1]/div/div[2]/div[1]/div/button'
    nameBox = '/html/body/div[3]/div[3]/div/section/div/div[1]/input'
    categoryBox = '/html/body/div[3]/div[3]/div/section/div/div[2]/div/select'
    statusBox = '/html/body/div[3]/div[3]/div/section/div/div[3]/div/select'
    unitBox = '/html/body/div[3]/div[3]/div/section/div/div[4]/div/select'
    saveBox = '/html/body/div[3]/div[3]/div/section/footer/button[1]'
    toastTitle = '/html/body/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]'
    deleteButton = '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[1]/div[5]/div/button[2]'
    toastDel = '/html/body/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]'
    editButton = '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[1]/div[5]/div/button[1]'
    toastEdit = '/html/body/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]'


class ProductsPage():

    def __init__(self, driver):
        self.driver = driver
        self.productsButton = Locators.productsButton
        self.prductsListTitle = Locators.productListTitle
        self.createProductBox = Locators.createProductBox
        self.nameBox = Locators.nameBox
        self.categoryBox = Locators.categoryBox
        self.statusBox = Locators.statusBox
        self.unitBox = Locators.unitBox
        self.saveBox = Locators.saveBox
        self.toastTitle = Locators.toastTitle
        self.deleteButton = Locators.deleteButton
        self.toastDel = Locators.toastDel
        self.editButton = Locators.editButton
        self.toastEdit = Locators.toastEdit

    def clickProducts(self):
        self.driver.find_element(By.XPATH, self.productsButton).click()
        time.sleep(1)

    def verifyProductsTitle(self):
        self.driver.implicitly_wait(10)
        self.title = self.driver.find_element(By.XPATH, self.prductsListTitle).text
        print(f"title: {self.title}")
        assert "product list" in self.title.lower()
        print("product list verified")

    def clickCreateBox(self):
        self.driver.find_element(By.XPATH, self.createProductBox).click()
        time.sleep(2)

    def setName(self, name):
        self.driver.find_element(By.XPATH, self.nameBox).send_keys(name)
        time.sleep(1)

    def clickCategory(self, category):
        Select(self.driver.find_element(By.XPATH, self.categoryBox)).select_by_value(category)
        time.sleep(1)

    def clickStatus(self, status):
        Select(self.driver.find_element(By.XPATH, self.statusBox)).select_by_value(status)
        time.sleep(1)

    def clickUnit(self, unit):
        Select(self.driver.find_element(By.XPATH, self.unitBox)).select_by_value(unit)
        time.sleep(1)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.saveBox).click()

    def verifySuccess(self):

        try:
            self.driver.implicitly_wait(10)
            self.toastEl = self.driver.find_element(By.XPATH, self.toastTitle).text
            print(f"toast message: {self.toastEl}")
            assert "product created" in self.toastEl.lower()
            print("toast message verified, product created")

        except Exception as e:
            print(f"failed to verify toast message: {str(e)}")

    def clickDelete(self):
        self.driver.find_element(By.XPATH, self.deleteButton).click()
        time.sleep(1)

    def deleteToast(self):

        try:
            self.driver.implicitly_wait(10)
            self.delToast = self.driver.find_element(By.XPATH, self.toastDel).text
            print(f"toast message: {self.delToast}")
            assert "product deleted" in self.delToast.lower()
            print("toast message verified, product deleted")

        except Exception as e:
            print(f"failed to verify toast message: {str(e)}")

    def clickEdit(self):
        self.driver.find_element(By.XPATH, self.editButton).click()
        time.sleep(1)

    def editToast(self):
        try:
            self.driver.implicitly_wait(10)
            self.updateToast = self.driver.find_element(By.XPATH, self.toastEdit).text
            print(f"toast message: {self.updateToast}")
            assert "product updated" in self.updateToast.lower()
            print("toast message verified, product updated")

        except Exception as e:
            print(f"failed to verify toast message: {str(e)}")