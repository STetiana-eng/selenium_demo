
import requests
from driver import Driver
from user_login import LoginPage
from garage_page import GaragePage


class TestAuthentication:
    def setup_class(self):
        self.driver = Driver.get_ChromiumEdge_driver()
        self.user_login = LoginPage()
        self.garage_page = GaragePage()
        self.session = requests.session()


    def setup_method(self):
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    def test_check_login_window(self):
        self.user_login.get_sign_in_button().click()
        assert self.user_login.get_email_field().is_displayed()

    def test_check_successful_login(self):
        self.user_login.get_sign_in_button().click()
        self.user_login.get_email_field().fill_field("test1234ts@rs.fd")
        self.user_login.get_password_field().fill_field("Qwerty123")
        self.user_login.get_login_button().click()
        assert self.garage_page.get_my_profile_button().is_displayed()


