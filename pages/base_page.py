from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def do_click(self,by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator)).click()

    def send_key(self,by_locator,data):
        self.wait.until(EC.visibility_of_element_located(by_locator)).send_keys(data)

    def get_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).text

    def get_title(self):
        return self.driver.title

    def is_displayed(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).is_displayed()