from selenium import webdriver
import time
#1.打开浏览器：实例化driver句柄(把柄)，Chrome：大写的c
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
driver.get("https://www.eastmoney.com")
#浏览器最大化
driver.maximize_window()

print(driver.title)
driver.find_element_by_link_text('财经').click()
time.sleep(3)
driver.switch_to_window(driver.window_handles[-1])
e = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div[2]/a[2]')
print(e.text)