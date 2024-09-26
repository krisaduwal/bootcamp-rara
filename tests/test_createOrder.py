from tests.test_logIn import *
from pages.createOrder import CreateOrderPage

class CreateOrderTest(LogIn):
    @classmethod
    def setUpClass(cls):
        LogIn.setUpClass()
        print("setting up")

    def test_createRecurringOrder(self):
        self.test_logIn()
        # LogIn.test_logIn(self.driver)
        driver = self.driver
        createOrder = CreateOrderPage(driver)
        createOrder.clickCreateBox()
        # driver.current_window_handle
        # driver.window_handles
        # self.driver.switch_to.window()
        createOrder.verifyTitle()

        createOrder.clickCustomerBox("Himal Lubricants Pvt.Ltd")
        createOrder.clickNext()
        createOrder.clickBranchBox("Himal Lubricants Pvt.Ltd B2")
        # createOrder.selectLocation("Lalitpur, Nepal")
        createOrder.clickNextButton()
        createOrder.clickBulkDelivery("Premium Petrol - gallons")
        createOrder.clickCheckbox()
        createOrder.inputQuantity("500")
        createOrder.clickSelectDriver("Rohan Magar")
        createOrder.clickAssetCategory("Truck")
        createOrder.enableReccuring()
        createOrder.clickFrequency("daily")
        # createOrder.clickRecuringEndDate("09/02/2024 11:11 AM")
        createOrder.clickCreateOrder()
        createOrder.verifySuccess()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()