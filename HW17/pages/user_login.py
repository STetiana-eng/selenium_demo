from selenium.webdriver.common.by import By
from base_page_with_driver import BasePageWithDriver
from HW17.controls.button import Button
from HW17.controls.textbox import TextBox
from HW17.controls.base_control import BaseControl


class LoginPage(BasePageWithDriver):
    def __init__(self):
        super().__init__()
        self._sign_in_button = None
        self._email_field = None
        self._password_field = None
        self._login_button = None

    def get_sign_in_button(self):
        self._sign_in_button = Button(self._driver.find_element(By.XPATH, "//button[text()='Sign In']"))
        return self._sign_in_button

    def get_email_field(self):
        self._email_field = TextBox(self._driver.find_element(By.ID, "signinEmail"))
        return self._email_field

    def get_password_field(self):
        self._password_field = TextBox(self._driver.find_element(By.ID, "signinPassword"))
        return self._password_field

    def get_login_button(self):
        self._login_button = Button(self._driver.find_element(By.XPATH, "//button[text()='Login']"))
        return self._login_button