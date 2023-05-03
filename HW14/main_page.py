from button import Button
from selenium.webdriver.common.by import By
from base_page import BasePage


class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        self.__View_All_Orders_button: Button = None

    def get_catalog_button(self):
        self.__View_All_Orders_button = Button(self._driver.find_element(By.XPATH, "//*[@id=\"latest-orders-card\"]/div[1]/h3/a"))
        return self.__View_All_Orders_button