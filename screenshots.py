from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\Program Files\Google\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")
#driver.save_screenshot("C:\SeleniumPractice\Captured\Homepage.png")
driver.get_screenshot_as_file("C:\SeleniumPractice\Captured\Home.png")