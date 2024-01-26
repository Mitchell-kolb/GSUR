from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pyperclip, os
from dotenv import load_dotenv

# Sets up driver and opens browser
driver = webdriver.Chrome()  ### NEED CHROME WEBDRIVERS TO BE RELEASED
driver.get("https://emma-back.mse.psych.wsu.edu/login")

# Sets Screen Size
driver.set_window_size(720, 790)  # fullscreen size is 1440 x 790 for Mitchell's machine

# Sets Window Location
screen_width = driver.execute_script("return window.screen.width;")
driver.set_window_position(screen_width // 2, 0)

#This uses JavaScript to check the readyState of the document. When the readyState is "complete", it means the webpage has finished loading
WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

#Login Credentials
load_dotenv()
env_username = os.getenv("USERNAME")
env_password = os.getenv("PASSWORD")
#print(env_password, env_username)
signInBoxUsername = driver.find_element(By.ID, 'inputUsername')
signInBoxUsername.send_keys(env_username)
signInBoxPassword = driver.find_element(By.ID, 'inputPassword')
signInBoxPassword.send_keys(env_password)
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

    #Counts all file items in the list
    rows = len(driver.find_elements(By.XPATH, '/html/body/div/div/div/table/tbody/tr'))
    print(rows-1)

    #Get the current working directory (where the web script is located)
    currentDirectory = os.path.dirname(os.path.realpath(__file__))
    print("Current directory:", currentDirectory)
    #Checks/creates a People folder in this directory.
    dirPath = currentDirectory + "/People"
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)


    #Loops through files and downloads them
    for r in range(2, 7):
        # Find the file list on webpage
        xpath = f'/html/body/div/div/div/table/tbody/tr[{r}]'
        fileCurrent = driver.find_element(By.XPATH, xpath)
        fileTitle = fileCurrent.text
        # Define the file path including the file name
        filePath = os.path.join(dirPath, f"{fileTitle}.txt")
        
        # Click into the files and copy its contents then go back to the file listing page
        fileCurrent.click()
        #sleep(1)
        fileContent = driver.find_element(By.XPATH, '/html/body/pre').text
        driver.execute_script("window.history.go(-1)")
        
        # Open the file in write mode ('w') and write the content from the selected file into it
        with open(filePath, "w") as file:
            file.write(fileContent)
        # Print the title to the screen
        print(fileTitle)



except Exception as e:
    print(f"An unexpected error occurred: {e}")


#Prints clipboard
#isCopied = pyperclip.paste()
#print("Clipboard:\t", isCopied)
#Looping

#Waits until the browser window is closed then closes the script and driver
try:
    # Wait until there are no open windows
    WebDriverWait(driver, 9999999).until(EC.number_of_windows_to_be(0))
finally:
    print('Session Ended')
    driver.quit()

