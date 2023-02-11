from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass



class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        # driver = webdriver.Chrome(executable_path="C:/Users/AFisenko/chromedriver.exe")
        # driver.get("https://rahulshettyacademy.com/angularpractice/")
        # driver.maximize_window()
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        # driver.find_element(By.CSS_SELECTOR, "[name='name']").send_keys("Rahul")
        homepage.getEmail().send_keys(getData["lastname"])
        # driver.find_element(By.NAME, "email").send_keys("shetty")
        homepage.getCheckBox().click()
        # driver.find_element(By.ID, "exampleCheck1").click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        # sel = Select(homepage.getGender())
        # sel = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        # sel.select_by_visible_text("Male")
        homepage.getSubmit().click()
        # driver.find_element(By.XPATH, "//input[@value = 'Submit]").click()
        alertText = homepage.getSuccessMessage().text
        # alertText = driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text

        assert ("Success" in alertText)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
