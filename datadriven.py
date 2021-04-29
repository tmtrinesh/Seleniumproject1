import XLUtils
from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\Program Files\Google\chromedriver_win32\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
path="C:\SeleniumPractice\Login.xlsx"
rows=XLUtils.getRowCount(path,'Sheet1')
for r in range(2,rows+1):
    username=XLUtils.readData(path,"Sheet1",r,1)
    password=XLUtils.readData(path,"Sheet1",r,2)
    driver.find_element_by_name("txtUsername").send_keys(username)
    driver.find_element_by_name("txtPassword").send_keys(password)
    driver.find_element_by_name("Submit").click()
    if driver.title=="menu_dashboard_index":
        print("test is passed")
        XLUtils.writeData(path,"Sheet1",r,3,"test passed")
    else:
        print("test failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed")
    driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")