import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class WebAutomation:

    def setupDriver(self):
        global driver
        driver = webdriver.Chrome()
        return driver

    def defineURL(self):
        url = 'https://www.mockaroo.com/'
        return url

    def openBrowser(self, url):
        driver.get(url)
        driver.find_element(By.XPATH, r'//*[@id="__next"]/main/div[2]/button[1]/span[1]').click()
        time.sleep(5)

    def print_page_title(self):
        return driver.title

    def tear_down(self):
        driver.close()

if __name__ == '__main__':
    web_auto_obj = WebAutomation()
    web_auto_obj.setupDriver()
    res_url = web_auto_obj.defineURL()
    web_auto_obj.openBrowser(res_url)
    res_title = web_auto_obj.print_page_title()
    web_auto_obj.tear_down()
