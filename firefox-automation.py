from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pyperclip

# Sets up driver and opens browser
driver = webdriver.Firefox()
driver.get("https://emma-back.mse.psych.wsu.edu/login")

# Sets Screen Size
driver.set_window_size(720, 790)  # fullscreen size is 1440 x 790 for Mitchell's machine

# Sets Window Location
screen_width = driver.execute_script("return window.screen.width;")
driver.set_window_position(screen_width // 2, 0)

#This uses JavaScript to check the readyState of the document. When the readyState is "complete", it means the webpage has finished loading
WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

#Login Credentials
signInBoxUsername = driver.find_element(By.ID, 'inputUsername')
signInBoxUsername.send_keys('mitchellk1')
signInBoxPassword = driver.find_element(By.ID, 'inputPassword')
signInBoxPassword.send_keys('mitchellk1')
signInButton = driver.find_element(By.XPATH, '/html/body/div/form[1]/button')
signInButton.click()

#Goes to the training files tab of the website
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
    #Gets title of the first item
    title = driver.find_element(By.XPATH, '/html/body/div/div/div/table/tbody/tr[2]').text
    print(title)
    
    #Clicks on the first file item
    #title = driver.find_element(By.XPATH, '/html/body/div/div/div/table/tbody/tr[2]')
    #title.click()

    #Counts all file items in the list
    rows = len(driver.find_elements(By.XPATH, '/html/body/div/div/div/table/tbody/tr'))
    print(rows-1)

    #Prints off the first 9 file items in the list as proof of concept
    #Open a file for writing
    with open('output-title.txt', 'w') as file:
        for r in range(2, 11):
            xpath = f'/html/body/div/div/div/table/tbody/tr[{r}]'
            title = driver.find_element(By.XPATH, xpath).text
            # Append the title to the file
            file.write(title + '\n')
            # Print the title to the screen
            print(title)

except Exception as e:
    print(f"An unexpected error occurred: {e}")


#Prints clipboard
#isCopied = pyperclip.paste()
#print("Clipboard:\t", isCopied)

#Waits until the browser window is closed then closes the script and driver
try:
    # Wait until there are no open windows
    WebDriverWait(driver, 9999999).until(EC.number_of_windows_to_be(0))
finally:
    print('Session Ended')
    driver.quit()

