import pytest
from selenium import webdriver

from pages.base_page import Base
from pages.login_page import Login
from test_cases.baseclass import TestBase


@pytest.mark.usefixtures("setup")
class Test_Login(TestBase):

    def test_login_with_valid_creds(self):
        self.login.do_the_login("student", "Password123")
        Expected_result = "Logged In Successfully"
        assert self.base.get_text(self.login.after_succesfull_login_text) == Expected_result

    def test_02_login_with_invalid_usernmae(self):
        self.login.do_the_login("stud", "Password123")
        Expected_result = "Your username is invalid!"
        assert self.base.get_text(self.login.invalid_usernmae_text_message) == Expected_result

    def test_03_login_with_invalid_password(self,setup):
        self.login.do_the_login("student", "Password")
        Expected_result = "Your password is invalid!"
        assert self.base.get_text(self.login.invalid_usernmae_text_message) == Expected_result

    def test_04_verify_title(self,setup):
        Expected_result = "Test Login | Practice Test Automation"
        assert self.base.get_title() == Expected_result

    def test_04_verify_logo_is_display(self):
        assert self.base.is_displayed(self.login.logo_display) == True










