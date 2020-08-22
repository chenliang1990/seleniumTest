#导入selenium
from selenium import webdriver

#1.打开浏览器：实例化driver句柄(把柄)，Chrome：大写的c
driver = webdriver.Chrome(executable_path = "chromedriver.exe")

#2.打开网页
# driver.get("https://www.baidu.com/")

#id定位
# driver.find_element_by_id("kw").send_keys("在我的地盘就得听我的")

# xpath定位
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys("在我的地盘就得听我的")

# name定位
# driver.find_element_by_name("wd").send_keys("在我的地盘就得听我的")

# class定位
# driver.find_element_by_class_name("s_ipt").send_keys("在我的地盘就得听我的")

# css selector
# driver.find_element_by_css_selector('#kw').send_keys("在我的地盘就得听我的")

# driver.find_element_by_id("su").click()
#超链接专用定位方式
# driver.find_element_by_link_text('高考加油').click()
# driver.find_element_by_partial_link_text('高考加').click()

#标签定位(基本不用)
# driver.find_element_by_tag_name("input")

