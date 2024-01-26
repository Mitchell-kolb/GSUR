


import os

# Get the current working directory (where the script is located)
current_directory = os.path.dirname(os.path.realpath(__file__))
print("Current directory:", current_directory)
# Checks/creates a the People folder in this directory.
dir_path = current_directory + "/Spotify"
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
else:
    print("Already exists")


""" 
def DJC_download_file():
    #Code to download a file from the web backend using login admin. You will need to replace "pwd" with the admin password. You may want to rename downloaded_file.txt as needed. Note you will probably need to install the requests Python module on your machine.
    
    import requests
    from requests.auth import HTTPBasicAuth

    # URL of the remote file you want to download
    file_url = "https://emma-back.mse.psych.wsu.edu/login"

    # Local file path where you want to save the downloaded file
    local_file_path = "/Users/mitchellkolb/Downloads/GSUR/People/"

    username = 'mitchellk1'
    password = 'mitchellk1'

    try:
        # Send an HTTP GET request to the remote URL with authentication
        response = requests.get(file_url, auth=HTTPBasicAuth(username, password))

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the local file for writing in binary mode
            with open(local_file_path, 'wb') as local_file:
                # Write the content of the remote file to the local file
                local_file.write(response.content)
            print(f"File downloaded and saved as {local_file_path}")
        else:
            print(f"Failed to download the file. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")





if(__name__ == "__main__"):

    filename="ABtest1_2023-02-01 12-51-21"

    DJC_download_file()

 """