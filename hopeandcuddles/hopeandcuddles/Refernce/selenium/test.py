from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH, options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://techwithtim.net")
print(driver.title)

# print(driver.page_source)

search = driver.find_element(By.NAME, "s")
search.send_keys("thisisatest")
search.send_keys(Keys.RETURN)

# search.click()

# search.send_keys(Keys.RETURN)
time.sleep(100)



driver.quit()