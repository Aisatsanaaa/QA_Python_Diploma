from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import pytest


@pytest.fixture(scope='function')
def driver():
    options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument('user-data-dir=test-site')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.accept_untrusted_certs = True
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
