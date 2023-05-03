from button import Button
from selenium.webdriver.common.by import By
from base_page import BasePage


class LogIn(BasePage):
    def __init__(self):
      super().__init__()
      self.__LogIn: Button = None

    def LogIn_button(self):
        self.__LogIn = Button(self._driver.find_element(By.XPATH, "//*[@type=\"submit\"]"))
        return self.__LogIn

