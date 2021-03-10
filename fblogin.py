# import thư viện
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
# Khai báo browser
browser = webdriver.Chrome(executable_path="./chromedriver.exe")

# Mở thử một trang web
browser.get("http://facebook.com")
sleep(3)
# Điền thông tin vào input
txtUser = browser.find_element_by_id("email")
txtUser.send_keys("Dondo7")
sleep(2)
txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("Dondo7")
sleep(3)

# Submit form
txtPass.send_keys(Keys.ENTER)

sleep(5)
# Đóng trang web
browser.close()