from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    productTitle = (By.XPATH, "//div[@class='card h-100']")
    # product.find_element(By.XPATH, "div/button").click()
    productDiv = (By.XPATH, "div/button")
    # productName = product.find_element(By.XPATH, "div/h4/a").text
    productName1 = (By.XPATH, "div/h4/a")
    # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")
    # self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    firstCheckout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    # self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")


    def getProductTitles(self):
        return self.driver.find_elements(*CheckOutPage.productTitle)

    def getProductDiv(self):
        return self.driver.find_elements(*CheckOutPage.productDiv)

    def getProductName(self):
        return self.driver.find_element(*CheckOutPage.productName1)

    def checkOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOut)

    def firstCheckoutItems(self):
        return self.driver.find_element(*CheckOutPage.firstCheckout)










