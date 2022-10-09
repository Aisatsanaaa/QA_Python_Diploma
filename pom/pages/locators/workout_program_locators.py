from selenium.webdriver.common.by import By

menu = (By.CLASS_NAME, 'personal-menu__holder')
add_content = (By.PARTIAL_LINK_TEXT, 'Add Content')
create_w_program = (By.PARTIAL_LINK_TEXT, 'Create workout program')
goal_window = (By.CSS_SELECTOR, 'mat-radio-group[formcontrolname="planOfCoaching"]')
publish_plan = (By.CSS_SELECTOR, 'mat-radio-button[value="1"]')
appeared_text = (By.TAG_NAME, 'p')
next_button = (By.CSS_SELECTOR, 'button[type="submit"]')
by_page = (By.CSS_SELECTOR, 'mat-radio-group[formcontrolname="privateOrGym"]')
plan_definition = (By.CSS_SELECTOR, 'mat-step-header[aria-posinset="2"]')
plan_definition_window = (By.ID, 'cdk-step-content-7-1')

online_coaching = (By.CSS_SELECTOR, 'mat-radio-button[value="2"]')
sport_discipline = (By.CSS_SELECTOR, 'mat-select[formcontrolname="sporting_direction"]')
fitness = (By.PARTIAL_LINK_TEXT, 'Fitness')
