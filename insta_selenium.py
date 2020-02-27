import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"

driver = webdriver.Chrome("/Users/singhyogendra/Desktop/chromedriver")
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
id = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys("usernamme")
password = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys("password")

driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
time.sleep(3)
driver.find_element_by_class_name("_9AhH0").click()
scroll = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[1]/div/article[1]/div[1]/div/div/div[2]")
y = 1100

for i in range(1, 20):
    i = str(i)
    time.sleep(2)
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[1]/div/article["+i+"]/div[2]/section[1]/span[1]/button"))
    driver.execute_script("window.scrollTo(0, " + str(y) + ")")
    y += 1100
    time.sleep(1)
    
