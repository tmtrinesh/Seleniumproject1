from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":"C:\Downloadedfiles"})

driver=webdriver.Chrome(executable_path="C:\Program Files\Google\chromedriver_win32\chromedriver.exe",chrome_options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
#how to download text file
driver.find_element_by_id("textbox").send_keys("testin in python automation")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()
#to download pdf file
driver.find_element_by_id("pdfbox").send_keys("This is python testing pdf")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()
time.sleep(5)

driver.close()