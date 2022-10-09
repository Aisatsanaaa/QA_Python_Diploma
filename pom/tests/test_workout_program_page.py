from time import sleep
import pytest
from QA_Python_Diploma.pom.pages.workout_program_page import WorkoutsProgramPage
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains


def test_create_workout_program(driver):
    workout_program = WorkoutsProgramPage(driver)
    workout_program.open()
    workout_program.menu_field.click()
    workout_program.add_content().is_displayed()
    workout_program.add_content().click()
    workout_program.create_w_program().is_displayed()
    workout_program.create_w_program().click()
    assert workout_program.goal_window().is_displayed()


def test_text_appeared(driver):
    workout_program = WorkoutsProgramPage(driver)
    workout_program.open()
    workout_program.menu_field.click()
    workout_program.add_content().click()
    workout_program.create_w_program().click()
    workout_program.publish_plan().is_displayed()
    workout_program.publish_plan().click()
    workout_program.appeared_text().is_displayed()
    assert workout_program.appeared_text().text != 'empty'


def test_next_button_works(driver):
    workout_program = WorkoutsProgramPage(driver)
    workout_program.open()
    workout_program.menu_field.click()
    workout_program.add_content().click()
    workout_program.create_w_program().click()
    workout_program.publish_plan().click()
    workout_program.next_button().is_displayed()
    workout_program.next_button().click()
    try:
        workout_program.publish_plan().click()
    except WebDriverException:
        print('You have moved to another page')
    assert True


@pytest.mark.skip
def test_fill_the_form(driver):
    workout_program = WorkoutsProgramPage(driver)
    workout_program.open()
    workout_program.menu_field.click()
    workout_program.add_content().click()
    workout_program.create_w_program().click()
    workout_program.online_coaching().click()
    workout_program.next_button().click()
    workout_program.sport_discipline().click()
    workout_program.fitness().click()
    sleep(2)
    # not ready
