import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://qk.mrhkj.com/admin/common/login.html")
driver.maximize_window()

# 1. 获取已经登录的cookie
# time.sleep(20)
# 手动获取cookie，自己去登录网站一下
# print(driver.get_cookies())

# 2. 删除之前原有的cookie(因为登录网站的时候会自动给你一个cookie，即使你还没登录)，并添加已经登录的cookie
driver.delete_all_cookies()  # 删除cookie
cookie = {'domain': 'qk.mrhkj.com', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'n4jnb9gs6m335p53aaeb6t46i8'}
driver.add_cookie(cookie)   # 添加已经登录的cookie
driver.refresh()            # 刷新网站，使用已经登录的cookie访问,cookie的有效期为30天
