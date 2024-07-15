from selenium import webdriver
import pytest

from pages.base_page import Base
from pages.login_page import Login


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')

@pytest.fixture()
def setup(request):
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "Safari":
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome()

    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    request.cls.login = Login(driver)
    request.cls.base = Base(driver)
    yield driver
    driver.quit()
