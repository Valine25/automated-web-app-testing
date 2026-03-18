import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.driver_setup import get_driver
from pages.login_page import LoginPage

def test_login():
    driver = get_driver()
    login = LoginPage(driver)

    login.open()
    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    assert "You logged into a secure area!" in login.get_message()

    driver.quit()


def test_invalid_login():
    driver = get_driver()
    login = LoginPage(driver)

    login.open()
    login.enter_username("wrong")
    login.enter_password("wrong")
    login.click_login()

    assert "Your username is invalid!" in login.get_message()

    driver.quit()