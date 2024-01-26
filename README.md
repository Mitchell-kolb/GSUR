# GSUR


## To use 
- Make sure you have these installed
    - Python3
    - Webdrivers for your browser of choice 
        - Google Chrome:  https://chromedriver.chromium.org/downloads
            - NOTE: Lastest version of chrome doesn't have stable webdrivers but you can download test previous chrome version that can work. As long as the version and webdriver match
            - Check here for lastest update: https://googlechromelabs.github.io/chrome-for-testing/
                - Need Help?  
                    - MacOS: https://www.youtube.com/watch?v=m4-Z5KqDHpU
                    - Windows: NA
        - Firefox:  https://github.com/mozilla/geckodriver/releases
            - Need Help?  
                - MacOS: https://www.youtube.com/watch?v=SlC1pd8EBNY or https://www.youtube.com/watch?v=J2GssX9NMOk 
                - Windows: https://www.youtube.com/watch?v=VSDWqbc8wig 
        - Safari: Safari has webdrivers built into the browser you just have to enable them
            - Safari > Preferences > Advanced Tab > Show Developer Menu in Menu Bar
            - Then Safari > Develop > Select Allow Remote Automation
            - Need Help?  https://www.youtube.com/watch?v=URt4t4e4Hs0 
- Create a virtual environment if you choose to do so
    - In the /GSUR folder
    - `python -m venv myenv`
    - On Windows `myenv/Scripts/activate`
    - On macOS and Linux `source myenv/bin/activate`
- Managing the virtual environment
    - When you want to leave use `deactivate`
    - Make sure to upgrade pip `python -m pip install --upgrade pip`
- Install packages from requirements.txt before running the Living Atlas
    - `pip install -r requirements.txt`
- For logging into the site you have to have your username and password setup for the automation to use
    - Create a new file `.env` in the same directory as the chrome_automation.py file and have it contain this:
        ```
        USERNAME = "your_username"
        PASSWORD = "your_password"
        ```


### To Run the GSUR Web Automation
- In 1st terminal navigate to the /GSUR folder 
    - Use `python3 chrome-automation.py` to run the chrome code
    - Use `python3 firefox-automation.py` to run the firefox code
    - Use `python3 safari-automation.py` to run the safari code
