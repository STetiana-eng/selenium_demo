# Write a test to log in on the website https://admin-demo.nopcommerce.com/
#
# Credentials:
#
# Login - admin@yourstore.com
# Password - admin
# Enter the login and password fields and click the login button. Check that login was successful


# Test: if 2 fields (login and password) are empty

from selenium import webdriver
from selenium.webdriver.common.by import By
from locators_constants import LocatorsConstants




def test_login():
    driver = webdriver.ChromiumEdge()
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.find_element(By.XPATH, LocatorsConstants.EMAIL_FIELD_XPATH).send_keys("admin@yourstore.com") #  should use if field is empty
    driver.find_element(By.XPATH, LocatorsConstants.PASSWORD_FIELD_XPATH).send_keys("admin") #  should use if field is epmty
    driver.find_element(By.XPATH, LocatorsConstants.LOGIN_BUTTON_XPATH).click()
    logout_button = driver.find_element(By.XPATH, LocatorsConstants.LOGOUT_BUTTON_XPATH)
    assert logout_button.is_displayed()
