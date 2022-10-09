from selenium.webdriver.common.by import By

member_login_button = (By.CSS_SELECTOR, 'span[class="head-control__icon icon-font_finger-print"]')

email_field = (By.CSS_SELECTOR, 'input[placeholder="Login or E-mail*"]')
password_field = (By.CSS_SELECTOR, 'input[placeholder="Password*"]')
enter_button = (By.CSS_SELECTOR, 'button[type="submit"]')
user = (By.CLASS_NAME, 'item')
