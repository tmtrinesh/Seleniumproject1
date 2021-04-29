from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\Program Files\Google\chromedriver_win32\chromedriver.exe")
driver.get("http://automationtesting.in/")
driver.maximize_window()  #maxixmize window
#driver.execute_script("window.scrollBy(0,1000)","")   #scrolldown by pixel
#flag=driver.find_element_by_xpath("//*[@id='footer']/div[2]/div[2]/div[2]/div/div/a")
#driver.execute_script("arguments[0].scrollIntoView();",flag)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")