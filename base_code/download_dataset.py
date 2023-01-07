"""
This Script automates the download of a CSV Dataset with 3 cols x 10 rows from mockaroo.com
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'https://www.mockaroo.com/'


class Download_Dataset:

    def setup_driver(self):
        global driver
        driver = webdriver.Chrome()

    def define_url(self):
        driver.get(URL)
        driver.maximize_window()
        time.sleep(2)

    def delete_rows(self):
        del_row = driver.find_element(By.XPATH,
                                      '//*[@id="__next"]/main/div[3]/form/div/div[3]/div/div[2]/div[6]/div[4]/button[2]')
        del_row.click()
        del_row = driver.find_element(By.XPATH,
                                      '//*[@id="__next"]/main/div[3]/form/div/div[3]/div/div[2]/div[5]/div[4]/button[2]')
        del_row.click()
        del_row = driver.find_element(By.XPATH,
                                      '//*[@id="__next"]/main/div[3]/form/div/div[3]/div/div[2]/div[4]/div[4]/button[2]')
        del_row.click()

    def rename_rows(self):
        rename_row = driver.find_element(By.XPATH,
                                         '//*[@id="__next"]/main/div[3]/form/div/div[3]/div/div[2]/div[1]/div[2]/div/div/input')
        rename_row.click()
        rename_row.send_keys(Keys.DELETE)
        time.sleep(2)
        rename_row.send_keys('id')
        time.sleep(2)
        rename_row = driver.find_element(By.XPATH,
                                         '//*[@id="__next"]/main/div[3]/form/div/div[3]/div/div[2]/div[2]/div[2]/div/div/input')
        rename_row.click()
        rename_row.send_keys(Keys.DELETE)
        time.sleep(2)
        rename_row.send_keys('full_name')
        time.sleep(2)

        rename_row = driver.find_element(By.XPATH,
                                         '//*[@id="__next"]/main/div[3]/form/div/div[3]/div/div[2]/div[3]/div[2]/div/div/input')
        rename_row.click()
        rename_row.send_keys(Keys.DELETE)
        time.sleep(2)
        rename_row.send_keys('address')
        time.sleep(2)

    def define_number_of_rows(self):
        define_nr_rows = driver.find_element(By.XPATH,
                                             '//*[@id="__next"]/main/div[3]/form/div/div[6]/div/div[1]/div/input')
        define_nr_rows.click()
        define_nr_rows.send_keys(Keys.DELETE)
        time.sleep(2)
        define_nr_rows.send_keys('10')
        time.sleep(2)

    def download_dataset(self):
        download_btn = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div[1]/button')
        download_btn.click()
        time.sleep(2)


if __name__ == '__main__':
    dataset_obj = Download_Dataset()
    dataset_obj.setup_driver()
    dataset_obj.define_url()
    dataset_obj.delete_rows()
    dataset_obj.rename_rows()
    dataset_obj.define_number_of_rows()
    dataset_obj.download_dataset()
    time.sleep(5)
