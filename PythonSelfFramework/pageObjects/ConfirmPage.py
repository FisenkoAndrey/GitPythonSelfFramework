from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    sendValue = (By.CSS_SELECTOR, "#country")
    # self.driver.find_element(By.LINK_TEXT, "India").click()
    acceptValue = (By.LINK_TEXT, "India")
    # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    termConditions = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
    finalSubmit = (By.XPATH, "//input[@type='submit']")

    def sendValueInd(self):
        return self.driver.find_element(*ConfirmPage.sendValue)

    def acceptValueIndia(self):
        return self.driver.find_element(*ConfirmPage.acceptValue)

    def termConditionsCheck(self):
        return self.driver.find_element(*ConfirmPage.termConditions)

    def finalSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.finalSubmit)