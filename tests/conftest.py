import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser_init():
    driver = webdriver.Chrome()
    return driver
