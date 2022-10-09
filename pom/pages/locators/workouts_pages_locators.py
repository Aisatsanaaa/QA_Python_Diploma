from selenium.webdriver.common.by import By

menu = (By.CLASS_NAME, 'personal-menu__holder')
workouts_plans = (By.LINK_TEXT, 'Workouts Plans')
workouts_plans_logo = (By.LINK_TEXT, 'Workouts Plans')

user_name_field = (By.CSS_SELECTOR, 'select[formcontrolname="currentCalendarPlan"]')
month = (By.XPATH, '/html/body/wodcat/section/calendar-plan/div/main/div[2]/div/div[1]/div[2]/div[1]/div[2]/h3')
month_arrow_right = (By.CSS_SELECTOR, 'i[class="icon-font_arrow-right"]')
window_workout = (By.CSS_SELECTOR, '[aria-label="Saturday October 22"]')
add_new_workout = (By.XPATH, '/html/body/wodcat/section/calendar-plan/div[2]/div/p')
simple_wod = (By.XPATH, '/html/body/wodcat/section/calendar-plan/div[2]/div/div/button[1]/span[1]')
header = (By.CLASS_NAME, 'title')

settings = (By.PARTIAL_LINK_TEXT, 'SETTINGS')
name_field = (By.CSS_SELECTOR, 'input[data-placeholder="Name"]')
button_save = (By.CSS_SELECTOR, 'button[class="mat-focus-indicator mat-stroked-button mat-button-base mat-primary"]')
updated = (By.CSS_SELECTOR, 'simple-snack-bar[class="mat-simple-snackbar ng-star-inserted"]')

wod_scoring = (By.ID, 'mat-select-value-1')
select_panel = (By.ID, 'mat-select-0-panel')
strength = (By.ID, 'mat-option-2')
modality = (By.ID, 'mat-select-value-3')
select_panel_two = (By.ID, 'mat-option-8')
description = (By.ID, 'mat-input-1')
number_of_rounds = (By.ID, 'mat-input-2')
time_limit = (By.ID, 'mat-input-3')
save_button = (By.CSS_SELECTOR, 'button[class="mat-focus-indicator mat-button mat-button-base mat-warn"]')
workout_calendar = (By.CLASS_NAME, 'workout-calendar')

workout_full = (By.PARTIAL_LINK_TEXT, '1')
workout_action = (By.CSS_SELECTOR, 'span[class="cal-event-title ng-star-inserted"]')
delete_workout = (By.CSS_SELECTOR, 'i[class="icon-font_cross"]')

discussion = (By.PARTIAL_LINK_TEXT, 'DISCUSSION')
type_a_comment = (By.CSS_SELECTOR, 'textarea[data-placeholder="Type a comment"]')
green_button = (By.CSS_SELECTOR, 'a[type="submit"]')
comment_list = (By.CSS_SELECTOR, 'ul[class="comments-list"]')
real_comment = (By.CLASS_NAME, 'comments-list__message-text')

delete_comment = (By.CSS_SELECTOR, 'a[class="ng-star-inserted"]')
