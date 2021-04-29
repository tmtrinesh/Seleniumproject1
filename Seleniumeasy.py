import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(executable_path="C:\Program Files\Google\chromedriver_win32\chromedriver.exe")
    request.cls.driver = driver
    driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.mark.usefixtures("setup")
class TestExample:

    @pytest.mark.smoke
    def test_title(self):
        print("Verify title...")
        assert "Selenium Easy" in self.driver.title

    @pytest.mark.smoke
    def test_content_text(self):
        print("Verify content on the page...")
        centertext = self.driver.find_element_by_css_selector('.tab-content .text-center').text
        assert "WELCOME TO SELENIUM EASY DEMO" == centertext

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_practicing(self):
        print("verifying exercise--")
        startpractisingBtn = self.driver.find_element_by_id('btn_basic_example')
        startpractisingBtn.click()
        time.sleep(10)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#basic .head')))