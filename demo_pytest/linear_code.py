import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(2)
driver.find_element("id", "user-name").send_keys("standard_user")
driver.find_element("id", "password").send_keys("secret_sauce")
driver.find_element("id", "login-button").click()
time.sleep(2)
driver.find_element("xpath", '//button[@id="add-to-cart-sauce-labs-backpack"]').click()
time.sleep(2)
print("Item has been added to cart successfully")

