import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    # driver.Chrome(executable_path="C:/Users/AFisenko/chromedriver.exe")
    driver = webdriver.Chrome(executable_path="C:/Users/AFisenko/chromedriver.exe")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    # service_obj = Service("C:/Users/AFisenko/chromedriver.exe")
    # driver = webdriver.Chrome(service=service_obj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(4)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

