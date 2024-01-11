from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
#from selenium.webdriver.chrome.service import Service
from time import sleep
import pyperclip

driver = webdriver.Safari()
driver.maximize_window()
#driver.set_window_size(720, 790)#fullscreen size is 1440 x 790
#driver.set_window_position(0, 0)

""" driver.get("https://duckduckgo.com")
duckbox = driver.find_element(By.XPATH, '//*[@id="search_form_input_homepage"]')
duckbox.click()
print('Now sending keys')
duckbox.send_keys('PizzaHut')
driver.implicitly_wait(2)
 """
#driver.switch_to.new_window('tab')
driver.get("https://emma-back.mse.psych.wsu.edu/login")

#driver.get("https://seleniumhq.github.io")
#oaky = driver.current_window_handle
#print(oaky)
#wait = WebDriverWait(driver, 10)
#wait.until(EC.title_is("SeleniumHQ Browser Automation"))

#This uses JavaScript to check the readyState of the document. When the readyState is "complete", it means the webpage has finished loading
WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

signInBoxUsername = driver.find_element(By.ID, 'inputUsername')
signInBoxUsername.send_keys('mitchellk1')

signInBoxPassword = driver.find_element(By.ID, 'inputPassword')
signInBoxPassword.send_keys('mitchellk1')

signInButton = driver.find_element(By.XPATH, '/html/body/div/form[1]/button')
signInButton.click()

#driver.implicitly_wait(5)
sleep(2)
try:
    trainingButton = driver.find_element(By.PARTIAL_LINK_TEXT, 'Training Files')
    trainingButton.click()
except NoSuchElementException:
    print("Element not found. Please check your Xpath selector.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

#Loops through files and prints them
try:
    title = driver.find_element(By.XPATH, '/html/body/div/div/div/table/tbody/tr[1]').text
    print(title)
except Exception as e:
    print(f"An unexpected error occurred: {e}")



isCopied = pyperclip.paste()
print("Clipboard:\t", isCopied)
sleep(5)

driver.quit()
print('Session Ended')

