from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\Program Files\Google\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")
#capture all cookies created by browser
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)   #print all cookie pairs

#adding new cookie to browser

cookie={'name':'Mycookie','value':'1234567890'}
driver.add_cookie(cookie)

cookies=driver.get_cookies()
print(len(cookies))
print(cookies)
#deleting cookie
driver.delete_cookie('Mycookie')

cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))