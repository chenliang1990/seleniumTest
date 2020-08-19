from selenium import webdriver
import time
#1.打开浏览器：实例化driver句柄(把柄)，Chrome：大写的c
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
# 练习
# 使用selenium实现自己的账号取登录禅道
driver.get("http://81.68.125.221:9000/zentao/user-login")
#窗口最大化
driver.maximize_window()
driver.find_element_by_id("account").send_keys("liuyun")
driver.find_element_by_name("password").send_keys("a12345678")
driver.find_element_by_id("submit").click()
#等待网页加载完成
# time.sleep(5)

#如果网页在3秒加载完,剩下2秒跳过不等待
driver.implicitly_wait(5)
# 标题断言
# assert driver.title == "我的地盘 - 禅道"
# print("测试成功")
# 网页地址
# assert driver.current_url == "http://81.68.125.221:9000/zentao/my/"
# 元素的文本值
assert driver.find_element_by_xpath('//*[@id="userNav"]/li/a/span[1]').text == "流云"

# 退出测试，关闭浏览器
driver.quit()