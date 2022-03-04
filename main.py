from telnetlib import KERMIT
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver.v2 as uc
import os
driver = uc.Chrome(use_subprocess=True)



# driver.get("https://www.twitch.tv/cigdemt")
# login = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button/div/div")
# login.click()
# time.sleep(2)
# user = driver.find_element_by_id("login-username")
# user.send_keys("nickzshe")
# password = driver.find_element_by_id("password-input")
# password.send_keys("sayko1191200")
# loginButton = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button/div/div")
# loginButton.click()
# time.sleep(2)
# # driver.get("https://www.twitch.tv/migrosturkiye")
# # time.sleep(3)
# FollowButton = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div/div/div/button/div/div/div")
# FollowButton.click()
# time.sleep(5)
# # messageBox = driver.find_element_by_class_name("chat-wysiwyg-input__editor")
# # messageBox.click()
# # messageBox.send_keys("İyi Yayınlar Kardeşim")
# # messageBox.send_keys(Keys.RETURN)
# # time.sleep(2500)
# # time.sleep(20)
# # driver.quit()
# # print("Program Ended")


# # count_windows=int(input("Kaç adet pencere açılsın?: ")) #textbox'dan gelecek değer
# # for item in range(0,count_windows):
# #     driver_loop="driver"+str(count_windows)
# #     driver_loop = uc.Chrome(use_subprocess=True)
# #     driver_loop.get("https://tr.wikipedia.org/wiki/Anasayfa")
# #     count_windows-=1
# # time.sleep(1000)
