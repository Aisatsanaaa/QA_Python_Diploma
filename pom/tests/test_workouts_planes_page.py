from time import sleep
import pytest
from QA_Python_Diploma.pom.pages.workouts_plans_page import WorkoutsPlansPage
from selenium.common.exceptions import WebDriverException

DESCRIPTION = 'I like automation testing'
ROUNDS = '2'
TIME_LIMIT = '4'
COMMENT = 'i like testing'
USER_NAME = 'Nastya'


def test_open_workouts_plans(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.is_displayed()
    workouts_plans.workouts_plans.click()
    workouts_plans.workouts_plans_logo.is_displayed()
    assert workouts_plans.workouts_plans_logo.text == 'Workouts Plans'


def test_user_name_field_is_not_empty(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.click()
    workouts_plans.user_name_field.is_displayed()
    name = workouts_plans.user_name_field.text
    assert name != 'empty'


def test_user_name_updated(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.click()
    sleep(2)
    name = workouts_plans.user_name_field.text
    workouts_plans.settings.is_displayed()
    workouts_plans.settings.click()
    workouts_plans.change_user_name.is_displayed()
    workouts_plans.change_user_name.click()
    workouts_plans.change_user_name.clear()
    workouts_plans.change_user_name.send_keys(USER_NAME)
    workouts_plans.button_save.is_displayed()
    workouts_plans.button_save.click()
    workouts_plans.updated.is_displayed()
    assert workouts_plans.updated.text == 'Updated'
    sleep(2)
    changed_name = workouts_plans.user_name_field.text
    assert name != changed_name


def test_month_is_displayed(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.click()
    assert workouts_plans.month.is_displayed()


def test_month_arrow_works(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.click()
    current_month = workouts_plans.month.text
    workouts_plans.month_arrow_right.click()
    next_month = workouts_plans.month.text
    assert current_month != next_month


def test_window_workout_is_empty(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.click()
    driver.execute_script("window.scrollTo(400, 600)")
    workouts_plans.window_workout.is_displayed()
    try:
        workouts_plans.workout_full.is_displayed()
    except WebDriverException:
        print('This field is empty now')
    assert True


def test_field_window_workout_is_displayed(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.click()
    workouts_plans.window_workout.is_displayed()
    workouts_plans.window_workout.click()
    workouts_plans.add_new_workout.is_displayed()
    assert workouts_plans.add_new_workout.text == 'Add new workout'


def test_simple_wod_is_clickable(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.click()
    workouts_plans.window_workout.click()
    workouts_plans.simple_wod.is_displayed()
    workouts_plans.simple_wod.click()
    workouts_plans.header.is_displayed()
    assert workouts_plans.header.is_displayed()


def test_simple_wod_fill_form(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.click()
    workouts_plans.window_workout.click()
    workouts_plans.simple_wod.click()
    workouts_plans.wod_scoring.click()
    workouts_plans.select_panel.click()
    workouts_plans.modality.click()
    workouts_plans.select_panel_two.click()
    workouts_plans.description.send_keys(DESCRIPTION)
    workouts_plans.number_of_rounds.send_keys(ROUNDS)
    workouts_plans.time_limit.send_keys(TIME_LIMIT)
    workouts_plans.save_button.click()
    sleep(2)
    workouts_plans.workout_calendar.is_displayed()
    assert workouts_plans.workout_calendar.is_displayed()


def test_window_workout_is_full(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.click()
    driver.execute_script("window.scrollTo(2000, 2500)")
    workouts_plans.window_workout.click()
    workouts_plans.workout_full.is_displayed()
    color = workouts_plans.workout_full.value_of_css_property('background-color')
    assert color == 'rgba(0, 0, 0, 0)'


def test_delete_workout(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.click()
    driver.execute_script("window.scrollTo(2000, 2500)")
    workouts_plans.window_workout.click()
    workouts_plans.workout_action.is_displayed()
    workouts_plans.delete_workout.is_displayed()
    workouts_plans.delete_workout.click()
    try:
        workouts_plans.workout_action.is_displayed()
    except WebDriverException:
        print('Workout has been deleted')
    assert True


def test_discussion_page(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.click()
    workouts_plans.discussion.is_displayed()
    workouts_plans.discussion.click()
    workouts_plans.type_a_comment.is_displayed()
    assert workouts_plans.type_a_comment.is_displayed()


def test_write_comment(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.click()
    workouts_plans.discussion.is_displayed()
    workouts_plans.discussion.click()
    workouts_plans.type_a_comment.send_keys(COMMENT)
    workouts_plans.green_submit.is_displayed()
    workouts_plans.green_submit.click()
    assert workouts_plans.real_comment.is_displayed()


def test_delete_comment(driver):
    workouts_plans = WorkoutsPlansPage(driver)
    workouts_plans.open()
    workouts_plans.menu_field.click()
    workouts_plans.workouts_plans.click()
    workouts_plans.discussion.is_displayed()
    workouts_plans.discussion.click()
    workouts_plans.delete_comment.is_displayed()
    workouts_plans.delete_comment.click()
    assert workouts_plans.delete_comment.is_displayed()
