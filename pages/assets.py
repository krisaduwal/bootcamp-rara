import time

from pages.createOrder import *

class Locators():

    assetsButton = '/html/body/div[1]/div/div[1]/div/nav/a[1]'
    assetsTitle = '/html/body/div[1]/div/div[2]/div[1]/h2'
    createAssetBox = '/html/body/div[1]/div/div[2]/div[1]/div/button'
    assetID = '/html/body/div[3]/div[3]/div/section/div/div[1]/input'
    assetCategory = '/html/body/div[3]/div[3]/div/section/div/div[2]/div/select'
    assetStatus = '/html/body/div[3]/div[3]/div/section/div/div[3]/div/select'
    assetSave = '/html/body/div[3]/div[3]/div/section/footer/button[1]'
    assetToast = '/html/body/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]'
    assetEdit = '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div/button[1]'
    editCategory = '/html/body/div[3]/div[3]/div/section/div/div[1]/div/select'
    editStatus = '/html/body/div[3]/div[3]/div/section/div/div[1]/div/select'
    saveEdit = '/html/body/div[3]/div[3]/div/section/footer/button[1]'
    toastUpdated = '/html/body/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]'
    assetDelete = '/html/body/div[1]/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[1]/div[4]/div/button[2]'
    toastDeleted = '/html/body/div[1]/div/div[2]/div[3]/div/div/div[1]/div[2]'

class AssetsPage():

    def __init__(self, driver):
        self.driver = driver
        self.assetsButton = Locators.assetsButton
        self.assetsTitle = Locators.assetsTitle
        self.createAssetBox = Locators.createAssetBox
        self.assetID = Locators.assetID
        self.assetCategory = Locators.assetCategory
        self.assetStatus = Locators.assetStatus
        self.assetSave = Locators.assetSave
        self.assetToast = Locators.assetToast
        self.assetEdit = Locators.assetEdit
        self.editCategory = Locators.editCategory
        self.editStatus = Locators.editStatus
        self.saveEdit = Locators.saveEdit
        self.toastUpdated = Locators.toastUpdated
        self.assetDelete = Locators.assetDelete
        self.toastDeleted = Locators.toastDeleted

    def clickAssets(self):
        self.driver.find_element(By.XPATH, self.assetsButton).click()
        time.sleep(1)

    def verifyAssestsTitle(self):
        self.driver.implicitly_wait(10)
        self.title = self.driver.find_element(By.XPATH, self.assetsTitle).text
        print(f"title: {self.title}")
        assert "asset list" in self.title.lower()
        print("asset list verified")

    def clickCreateAsset(self):
        self.driver.find_element(By.XPATH, self.createAssetBox).click()
        time.sleep(2)

    def setID(self, id):
        self.driver.find_element(By.XPATH, self.assetID).send_keys(id)
        time.sleep(1)

    def setCategory(self, category):
        Select(self.driver.find_element(By.XPATH, self.assetCategory)).select_by_value(category)
        time.sleep(1)

    def setStatus(self, status):
        Select(self.driver.find_element(By.XPATH, self.assetStatus)).select_by_value(status)
        time.sleep(1)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.assetSave).click()

    def verifySuccess(self):

        try:
            self.driver.implicitly_wait(10)
            self.toastEl = self.driver.find_element(By.XPATH, self.assetToast).text
            print(f"toast message: {self.toastEl}")
            assert "asset created" in self.toastEl.lower()
            print("toast message verified, asset created")

        except Exception as e:
            print(f"failed to verify: {str(e)}")

    def clickEdit(self):
        self.driver.find_element(By.XPATH, self.assetEdit).click()
        time.sleep(1)

    def categoryEdit(self, category):
        Select(self.driver.find_element(By.XPATH, self.editCategory)).select_by_value(category)
        time.sleep(1)

    def statusEdit(self, status):
        Select(self.driver.find_element(By.XPATH, self.editStatus)).select_by_value(status)
        time.sleep(1)

    def editSave(self):
        self.driver.find_element(By.XPATH, self.saveEdit).click()

    def updateToast(self):

        try:
            self.driver.implicitly_wait(10)
            self.toastUp = self.driver.find_element(By.XPATH, self.toastUpdated).text
            print(f"toast message: {self.toastUp}")
            assert "asset updated" in self.toastUp.lower()
            print("toast message verified, asset updated")

        except Exception as e:
            print("failed to verify toast message")

    def clickDelete(self):
        self.driver.find_element(By.XPATH, self.assetDelete).click()
        time.sleep(1)

    def verifyDeleted(self):
        try:
            self.driver.implicitly_wait(5)
            self.delToast = self.driver.find_element(By.XPATH, self.toastDeleted).text
            print(f"toast message: {self.delToast}")
            assert "asset deleted" in self.delToast.lower()
            print("toast message verified, asset deleted")

        except:
            print("failed to verify")

