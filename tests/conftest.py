import pytest
from selenium import webdriver


def browser_init():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture(scope='session')
def page_title():
    res_driver = browser_init()
    res_driver.get('https://www.mockaroo.com/')
    return res_driver.title
