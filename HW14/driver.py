from selenium import webdriver
from selenium.webdriver.edge.webdriver import WebDriver


class Driver:
    driver = None

    @staticmethod
    def get_ChromiumEdge_driver() -> WebDriver:
        if Driver.driver is None:
            Driver.driver = webdriver.ChromiumEdge()
            return Driver.driver
        else:
            return Driver.driver
