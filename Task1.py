from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
search = driver.find_element(By.NAME, "q")
search.send_keys("Actor Suriya")
print(search.get_attribute("value"))
search.send_keys(Keys.ENTER)
input("Press Enter to close the browser...")
driver.quit()