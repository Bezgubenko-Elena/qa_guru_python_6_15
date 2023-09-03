import pytest
from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser_management():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.config.driver = driver
    yield
    browser.quit()
