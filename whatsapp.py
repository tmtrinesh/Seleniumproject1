from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\Program Files\Google\chromedriver_win32\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
input("please scan qr code and press any key to continue")
RM = driver.find_element_by_css_selector("")