import time

from tests.test_logIn import *
from pages.assets import AssetsPage

class CreateAsset(LogIn):

    @classmethod
    def setUpClass(cls):
        LogIn.setUpClass()

    def test_createAsset(self):
        self.test_logIn()
        driver = self.driver
        createAsset = AssetsPage(driver)
        createAsset.clickAssets()
        createAsset.verifyAssestsTitle()
        createAsset.clickCreateAsset()
        createAsset.setID("BA KHA 99")
        createAsset.setCategory("Tank Wagon")
        createAsset.setStatus("inactive")
        createAsset.clickSave()
        createAsset.verifySuccess()

    def test_edit(self):
        self.test_createAsset()
        time.sleep(5)
        driver = self.driver
        editAsset = AssetsPage(driver)
        editAsset.clickEdit()
        editAsset.categoryEdit("Wagon")
        editAsset.editSave()
        editAsset.updateToast()

    def test_delete(self):
        self.test_createAsset()
        time.sleep(5)
        driver = self.driver
        deleteAsset = AssetsPage(driver)
        deleteAsset.clickDelete()
        deleteAsset.verifyDeleted()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()