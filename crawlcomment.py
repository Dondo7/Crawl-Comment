# import thư viện
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
# Khai báo browser
browser = webdriver.Chrome(executable_path="./chromedriver.exe")

# Mở thử một trang web
browser.get("https://www.facebook.com/langthangDaNangg/posts/275870820565685")
sleep(3)

# Điền thông tin đăng nhập
txtUser = browser.find_element_by_id("email")
txtUser.send_keys("nf4114900@gmail.com")
sleep(2)

txtPass = browser.find_element_by_id("pass")
txtPass.send_keys("password123456")
sleep(3)

txtPass.send_keys(Keys.ENTER)
sleep(7)

# Lấy comment
#showcomment_link = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/span/a")
#showcomment_link.click()
#sleep(5)

showmore_link = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[4]/div[1]/div[2]/span/span")
showmore_link.click()
sleep(10)
showmore_link.click()
sleep(6)


# Đóng trang web
browser.close()