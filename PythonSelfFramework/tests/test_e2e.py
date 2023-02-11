import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass



# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):

        # browserSortedVeggies = []
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        # self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()
        checkOutPage = CheckOutPage(self.driver)
        log.info("getting all the card titles")
        products = checkOutPage.getProductTitles()
        #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for product in products:
            # productName = checkOutPage.getProductName().text
            productName = product.find_element(By.XPATH, "div/h4/a").text  # we chain these elements
            log.info(productName)
            if productName == "Blackberry":
                # checkOutPage.getProductDiv().click()
                product.find_element(By.XPATH, "div/button").click()

        checkOutPage.firstCheckoutItems().click()
        # self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        checkOutPage.checkOutItems().click()
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        confirmPage = ConfirmPage(self.driver)
        log.info("Entering country name as ind")
        confirmPage.sendValueInd().send_keys("ind")
        # self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")
        self.verifyLinkPresence("India")
        # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        confirmPage.acceptValueIndia().click()
        # self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.termConditionsCheck().click()
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirmPage.finalSubmitButton().click()
        # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        successText = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        log.info("Text received from application is " + successText)
        assert "Success! Thank you!" in successText  # not necessary to compare an entire text, we can compare a partial text in successText