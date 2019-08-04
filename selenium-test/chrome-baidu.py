# coding = utf-8

from selenium import webdriver
import time


option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

driver = webdriver.Chrome(options=option)
driver.get('https://cn.bing.com/')

driver.find_element_by_id("sb_form_q").send_keys("Selenium2")


driver.find_element_by_id("sb_form_go").click()
