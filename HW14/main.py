from driver import Driver
from Login import LogIn
from main_page import MainPage
from order_page import OrderPage


class TestOrder:
    def setup_class(self):
        self.driver = Driver.get_ChromiumEdge_driver()
        self.driver.maximize_window()
        self.Login = LogIn()
        self.main_page = MainPage()
        self.order_page = OrderPage()
    def setup_method(self):
        self.driver.maximize_window()
        self.driver.get("https://admin-demo.nopcommerce.com/")


    def test_get_order_page(self):
        self.Login.LogIn_button().click()
        self.main_page.get_catalog_button().click()
        result = self.order_page.get_certification_text()
        assert result == "Search"

    def teardown_method(self):
        pass

    def teardown_class(self):
        self.driver.quit()
