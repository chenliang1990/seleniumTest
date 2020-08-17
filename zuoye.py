from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.get("http://81.68.125.221:8080/ljindex/html/register.html")
driver.maximize_window()
driver.find_element_by_id("username").send_keys("chen1990")
driver.find_element_by_id("phonenum").send_keys("13775077374")
driver.find_element_by_id("password").send_keys("a12345678")
driver.find_element_by_id("confirpw").send_keys("a12345678")
driver.find_element_by_id("emailnum").send_keys("aa123a@qq.com")
driver.find_elements_by_id("userRegist").click()
time.sleep(5)


