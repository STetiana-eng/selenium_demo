from button import Button
from selenium.webdriver.common.by import By
from base_page import BasePage
from lable import Label


class OrderPage(BasePage):
    def __init__(self):
        super().__init__()
        self.__info: Label = None

    def get_certification_text(self):
        self.__info = Label(
           self._driver.find_element(By.XPATH, "//*[@id=\"search-orders\"]"))
        return self.__info.get_text()
