import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.implicitly_wait(10)
time.sleep(2)
googletitle=driver.title
exptitle="Google"
if googletitle==exptitle:
    print("The title of google is found correct and it is verified")
else:
    print("The title of google is found not correct and it is verified")
driver.close()
