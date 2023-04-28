from selenium import webdriver
from selenium.webdriver.common.by import By
# from locators_constants import LocatorsConstants
from selenium.webdriver.common.keys import Keys



driver = webdriver.ChromiumEdge()
driver.get("https://www.google.com")
driver.find_element(By.XPATH, "//*[text()='Alle akzeptieren']").click()
driver.implicitly_wait(120)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div").send_keys(123)
google_ico = driver.find_element(By.XPATH, "//img[@class='jfN4p']")
a=0



a = 0


