from time import sleep
import pytest

from QA_Python_Diploma.pom.pages.login_page import LoginPage


EMAIL = 'aaisatsana18@gmail.com'
PASSWORD = 'password1'


def test_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.member_login_button.click()
    login_page.email_field.is_displayed()
    login_page.password_field.is_displayed()
    login_page.email_field.click()
    login_page.email_field.send_keys(EMAIL)
    login_page.password_field.click()
    login_page.password_field.send_keys(PASSWORD)
    login_page.enter_button.click()
    login_page.user.is_displayed()
    assert login_page.user.is_displayed()
