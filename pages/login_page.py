from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import Base


class Login(Base):

    username = (By.ID, "username")
    password = (By.ID, "password")
    submit_btn = (By.ID,  "submit")
    after_succesfull_login_text = (By.CSS_SELECTOR, "h1[class='post-title")
    invalid_usernmae_text_message = (By.ID, "error")
    logo_display = (By.CSS_SELECTOR, "[class='custom-logo-link']")

    def do_the_login(self, username, password):
        self.send_key(self.username, username)
        self.send_key(self.password, password)
        self.do_click(self.submit_btn)