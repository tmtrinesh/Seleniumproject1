from selenium import webdriver
import time
from selenium.webdriver.common import action_chains

driver = webdriver.Chrome(executable_path="C:\Program Files\Google\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[1]/div[2]/div[3]/div/div/div/a")


#driver.find_element_by_css_selector("#nav-link-accountList")
 #driver.find_element_by_css_selector("#nav-flyout-ya-signin > a > span")
#a.click()

