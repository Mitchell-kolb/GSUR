# GSUR


## To use 
- Make sure you have these installed
    - Python3
    - Your browser of choice webdrivers
        - Google Chrome:  https://chromedriver.chromium.org/downloads
            - NOTE: Lastest version of chrome doesn't have stable webdrivers 
            - Check here for lastest update: https://googlechromelabs.github.io/chrome-for-testing/
                - Need Help?  
                    - MacOS: https://www.youtube.com/watch?v=m4-Z5KqDHpU&t=104s
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
    - In in the /GSUR folder
    - `python -m venv myenv`
    - On Windows `myenv/Scripts/activate`
    - On macOS and Linux `source myenv/bin/activate`
- Managing the virtual environment
    - When you want to leave use `deactivate`
    - Make sure to upgrade pip `python -m pip install --upgrade pip`
- Install packages from requirements.txt before running the Living Atlas
    - `pip install -r requirements.txt`


### To Run the GSUR Web Automation
- In 1st terminal navigate to the /GSUR folder 
    - Use `python3 firefox-automation.py` to run the firefox code
    - Use `python3 safari-automation.py` to run the safari code
    - Use `python3 chrome-automation.py` to run the google chrome code
