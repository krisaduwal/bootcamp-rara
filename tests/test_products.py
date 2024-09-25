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


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()