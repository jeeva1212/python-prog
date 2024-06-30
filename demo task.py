import time
from selenium import webdriver

from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/v1/")
time.sleep(1)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
act_title=driver.title
exp_title="Swag Labs"
if act_title==exp_title:
    print("Login page was succesfully")
else:
    print("failed to load page")

driver.find_element(By.XPATH,"//*[@id='menu_button_container']/div/div[3]/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='inventory_sidebar_link']").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,"inventory_item_name").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='menu_button_container']/div/div[3]/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='inventory_sidebar_link']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//*[@id='item_5_title_link']/div").click()
time.sleep(4)
driver.find_element(By.XPATH,"//*[@id='inventory_item_container']/div/div/div/button").click()
time.sleep(4)
driver.find_element(By.XPATH,"//*[@id='menu_button_container']/div/div[3]/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='inventory_sidebar_link']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//*[@id='item_1_title_link']/div").click()
time.sleep(4)
driver.find_element(By.XPATH,"//*[@id='menu_button_container']/div/div[3]/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='inventory_sidebar_link']").click()
time.sleep(4)

#driver.find_elements(By.XPATH,"btn_primary btn_inventory").click()
#driver.find_element(By.XPATH,"//*[@id="inventory_container"]/div/div[5]/div[3]/div").click()

"""links=driver.find_elements(By.TAG_NAME,"a")
print("Number of links present is:",len(links))
for link in links:
    print(link.text)
"""

driver.close()
