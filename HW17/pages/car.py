from selenium.webdriver.common.by import By
from base_page_with_driver import BasePageWithDriver
from HW17.controls.button import Button



class Add_a_car(BasePageWithDriver):
    def __init__(self):
        super().__init__()
        self.add_car_button = None
        self._brand = None
        self._model = None
        self._mileage = None

    def get_add_car_button(self):
        self._add_car_button = Button(self._driver.find_element(By.XPATH, "//button[text()='Add car']"))
        return self._add_car_button

    def get_brand(self):
        self._brand = self._driver.find_element(By.ID, "addCarBrand")
        return self._brand

    def get_model(self):
        self._model = self._driver.find_element(By.XPATH, "addCarModel")
        return self._model

    def get_mileage(self):
        self._mileage = self._driver.find_element (By.ID, "addCarMileage")
        return self._mileage

    def get_add(self):
        self._add = Button(self._driver.find_element(By.XPATH, "//button[text()='Add']"))
        return self._add


