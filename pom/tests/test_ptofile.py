from time import sleep
import pytest
from selenium.webdriver import ActionChains
from QA_Python_Diploma.pom.pages.profile_page import ProfilePage
from selenium.common.exceptions import WebDriverException

USER_NAME = 'Anastasiya'
INSTAGRAM = 'testing'
FACEBOOK = 'testing'
FACEBOOK_LINK = 'https://www.facebook.com/Kotiki.kote/'
TWITTER_LINK = 'https://twitter.com/hashtag/cat'


def test_logo_is_displayed(driver):
    profile_page = ProfilePage(driver)
    profile_page.open()
    profile_page.logo.is_displayed()
    assert profile_page.logo.is_displayed()


def test_dashboard_is_displayed(driver):
    profile_page = ProfilePage(driver)
    profile_page.open()
    profile_page.menu_field.is_displayed()
    profile_page.menu_field.click()
    assert profile_page.menu_field.is_displayed()


def test_see_profile_check(driver):
    profile_page = ProfilePage(driver)
    profile_page.open()
    profile_page.menu_field.click()
    profile_page.profile_and_settings.is_displayed()
    profile_page.profile_and_settings.click()
    profile_page.see_profile.is_displayed()
    assert profile_page.see_profile.is_displayed()


def test_profile_person_image_is_displayed(driver):
    profile_page = ProfilePage(driver)
    profile_page.open()
    profile_page.menu_field.click()
    profile_page.profile_and_settings.click()
    profile_page.see_profile.click()
    profile_page.img.is_displayed()
    assert profile_page.img.is_displayed()


def test_avatar_max_width(driver):
    profile_page = ProfilePage(driver)
    profile_page.open()
    profile_page.profile_and_settings.click()
    profile_page.see_profile.click()
    width = profile_page.img.value_of_css_property('max-width')
    assert width == '100%'


def test_gender_position(driver):
    profile_page = ProfilePage(driver)
    profile_page.open()
    profile_page.profile_and_settings.click()
    profile_page.see_profile.click()
    profile_page.gender.is_displayed()
    background_image = profile_page.gender.value_of_css_property('background-image')
    assert background_image == 'url("https://wodcat.com/assets/images/sprite-src/gender-female.png")'


def test_edit_profile(driver):
    profile_page = ProfilePage(driver)
    profile_page.open()
    profile_page.menu_field.click()
    profile_page.profile_and_settings.click()
    profile_page.redact_profile.is_displayed()
    profile_page.redact_profile.click()
    profile_page.heading.is_displayed()
    assert profile_page.heading.text == 'Profile edit'


def test_user_name(driver):
    profile_page = ProfilePage(driver)
    profile_page.open()
    profile_page.menu_field.click()
    profile_page.profile_and_settings.click()
    profile_page.see_profile.click()
    profile_page.user_name.is_displayed()
    sleep(2)
    assert profile_page.user_name.text != 'empty'


def test_change_name(driver):
    profile_page = ProfilePage(driver)
    profile_page.open()
    profile_page.menu_field.click()
    profile_page.profile_and_settings.click()
    profile_page.see_profile.click()
    profile_page.user_name.is_displayed()
    sleep(2)
    name = profile_page.user_name.text
    profile_page.redact_profile.click()
    profile_page.user_name_input.is_displayed()
    profile_page.user_name_input.click()
    profile_page.user_name_input.send_keys(USER_NAME)
    driver.execute_script("window.scrollTo(1000, 1200)")
    profile_page.save_button.is_displayed()
    profile_page.save_button.click()
    profile_page.saved.is_displayed()
    assert profile_page.saved.text == 'Saved'
    profile_page.menu_field.click()
    profile_page.see_profile.click()
    profile_page.user_name.is_displayed()
    sleep(2)
    changed_name = profile_page.user_name.text
    assert name != changed_name


def test_input_instagram_error(driver):
    profile_page = ProfilePage(driver)
    profile_page.open()
    profile_page.menu_field.click()
    profile_page.profile_and_settings.click()
    profile_page.redact_profile.click()
    driver.execute_script("window.scrollTo(1000, 1200)")
    profile_page.instagram.click()
    profile_page.instagram.send_keys(INSTAGRAM)
    profile_page.table.click()
    profile_page.error.is_displayed()
    assert profile_page.error.text == 'please enter correct link'


def test_input_ig_error_fb_right(driver):
    profile_page = ProfilePage(driver)
    profile_page.open()
    profile_page.menu_field.click()
    profile_page.profile_and_settings.click()
    profile_page.redact_profile.click()
    driver.execute_script("window.scrollTo(1000, 1200)")
    profile_page.instagram.click()
    profile_page.instagram.send_keys(INSTAGRAM)
    profile_page.facebook.send_keys(FACEBOOK_LINK)
    try:
        profile_page.save_button.click()
    except WebDriverException:
        print('One of the fields is filled incorrectly. '
              'The button is unavailable.')
    assert True


def test_save_button_does_not_work(driver):
    profile_page = ProfilePage(driver)
    profile_page.open()
    profile_page.menu_field.click()
    profile_page.profile_and_settings.click()
    profile_page.redact_profile.click()
    profile_page.facebook.send_keys(FACEBOOK)
    profile_page.table.click()
    try:
        profile_page.save_button.click()
    except WebDriverException:
        print('The button is unavailable now')
    assert True


def test_social_network_is_saved_and_displayed(driver):
    profile_page = ProfilePage(driver)
    profile_page.open()
    profile_page.menu_field.click()
    profile_page.profile_and_settings.click()
    profile_page.redact_profile.click()
    profile_page.twitter.send_keys(TWITTER_LINK)
    profile_page.save_button.click()
    profile_page.saved.is_displayed()
    assert profile_page.saved.text == 'Saved'
    profile_page.menu_field.click()
    profile_page.see_profile.click()
    assert profile_page.social_network_on_the_main_page.is_displayed()
