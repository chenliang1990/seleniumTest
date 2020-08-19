from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.get("http://81.68.125.221:8080/ljindex")
driver.maximize_window()
driver.find_element_by_link_text("登录").click()
time.sleep(3)
driver.find_element_by_id("username").send_keys("chen1990")
driver.find_element_by_id("password").send_keys("a12345678")
driver.find_element_by_id('userLogin').click()
time.sleep(3)
#点击确定按钮
# driver.switch_to_alert().accept()
#取消按钮
driver.switch_to_alert().dismiss()