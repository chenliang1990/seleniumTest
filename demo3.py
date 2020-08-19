from selenium import webdriver
from seleniumtools import find_element
#1.打开浏览器：实例化driver句柄(把柄)，Chrome：大写的c
driver = webdriver.Chrome(executable_path = "chromedriver.exe")
# 练习
# 使用selenium实现自己的账号取登录禅道
driver.get("http://81.68.125.221:9000/zentao/user-login")
#窗口最大化
driver.maximize_window()
username = ('id',"account")
password = ('name','password')
loginbtn = ('id','submit')
userInfo = ('xpath','//*[@id="userNav"]/li/a/span[1]')

find_element(driver,username).send_keys('liuyun')
find_element(driver,password).send_keys('a12345678')
find_element(driver,loginbtn).click()

assert find_element(driver,userInfo).text == "流云"
print("登录禅道成功!")