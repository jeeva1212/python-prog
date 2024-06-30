#Test case
#----------------------
# 1.open web browser (chrome/firefox/edge)
# 2.open URL https://opensource-demo.orangehrmlive.com/
# 3.Enter username (Admin)
# 4.Enter password (admin123)
# 5.click on login
# 6.capture title of the home page.(Actual title)
# 7.verify title of the page: OrangeHRM (Expected)
# 8.close browser


import time
from selenium import webdriver

from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(1)
