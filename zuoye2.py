from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.get("http://81.68.125.221:8080/ljindex/html/login.html")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("chen1990")
driver.find_element_by_id("password").send_keys("a12345678")

driver.find_element_by_xpath('//*[@id="userLogin"]').click()
time.sleep(5)
