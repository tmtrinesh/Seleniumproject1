from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\Program Files\Google\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to_frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C:\hanuman-chalisa.pdf")


