from HW17.model.create_post_car import CreatePostCar
import requests
from selenium.webdriver.common.by import By
from driver import Driver
from car import Add_a_car





class TestCar():
    def setup_class(self):
        self.driver = Driver.get_ChromiumEdge_driver()
        self.session = requests.session()
        self.car = Add_a_car()


    def setup_method(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    def test_check_login_window(self):
        self.car.get_add_car_button().click()
        assert self.car.get_brand().is_displayed()


    def test_check_successful_create_car(self):
        self.car.get_add_car_button().click()
        self.car.get_brand().click()
        self.car.get_model().click()
        self.car.get_mileage().click()
        self.car.get_add().click
        assert self._driver.find_element(By.XPATH, "//button[text()='Add fuel expense']").is_displayed()
