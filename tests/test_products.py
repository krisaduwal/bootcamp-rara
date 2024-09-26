import time

from tests.test_createOrder import *
from tests.test_logIn import *
from pages.products import ProductsPage

class CreateProduct(LogIn):

    @classmethod
    def setUpClass(cls):
        LogIn.setUpClass()
        print("setting up")

    def test_createProduct(self):
        self.test_logIn()
        driver = self.driver
        createProduct = ProductsPage(driver)
        createProduct.clickProducts()
        createProduct.verifyProductsTitle()
        createProduct.clickCreateBox()
        createProduct.setName("kris")
        createProduct.clickCategory(" Diesel")
        createProduct.clickStatus("available")
        createProduct.clickUnit("gallons")
        createProduct.clickSave()
        createProduct.verifySuccess()

    def test_deleteProduct(self):
        # self.test_createProduct()
        time.sleep(5)
        driver = self.driver
        deleteProduct = ProductsPage(driver)
        deleteProduct.clickDelete()
        deleteProduct.deleteToast()

    def test_editProduct(self):
        time.sleep(5)
        driver = self.driver
        driver.implicitly_wait(5)
        editProduct = ProductsPage(driver)
        editProduct.clickEdit()
        editProduct.clickStatus("out_of_stock")
        editProduct.clickSave()
        editProduct.editToast()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()