from selenium.webdriver.common.by import By

logo = (By.CLASS_NAME, 'logo__holder')
menu = (By.CLASS_NAME, 'personal-menu__holder')
profile_and_settings = (By.XPATH, '//span[text()="Profile and settings"]')

see_profile = (By.CSS_SELECTOR, 'a[href="/user/aisatsana"]')
profile_image = (By.CLASS_NAME, 'profile-person__image')
user_name = (By.TAG_NAME, 'h2')
edit_profile = (By.XPATH, '/html/body/wodcat/section/profile-page/div/main/section/div/div[1]/div/ul/li/a')
heading = (By.TAG_NAME, 'h1')

redact_profile = (By.CSS_SELECTOR, 'a[href="/account/profile/edit"]')
first_name = (By.CSS_SELECTOR, 'input[data-placeholder="First Name:"]')
button_save = (By.CSS_SELECTOR, 'button[class="mat-focus-indicator mat-button mat-button-base mat-primary"]')
saved = (By.CSS_SELECTOR, 'simple-snack-bar[class="mat-simple-snackbar ng-star-inserted"]')

img = (By.CSS_SELECTOR, 'img[class="ng-star-inserted"]')
gender = (By.CSS_SELECTOR, 'span[class="profile-icon_gender-female ng-star-inserted"]')

instagram = (By.CSS_SELECTOR, 'input[formcontrolname="ig"]')
table = (By.CLASS_NAME, 'profile-tabset')
error = (By.TAG_NAME, 'mat-error')

facebook = (By.CSS_SELECTOR, 'input[formcontrolname="fb"]')
twitter = (By.CSS_SELECTOR, 'input[formcontrolname="tw"]')
social_network_on_the_main_page = (By.TAG_NAME, 'a')