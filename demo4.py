from selenium import webdriver
import time
#1.打开浏览器：实例化driver句柄(把柄)，Chrome：大写的c
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.get("http://passport2.eastmoney.com/pub/login")
#浏览器最大化
driver.maximize_window()

#切换到小网页
frame = driver.find_element_by_id("frame_login")
driver.switch_to_frame(frame)

driver.find_element_by_id("txt_mobile").send_keys("123")
#切换到大网页
driver.switch_to_default_content()