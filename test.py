

import os

# Get the current working directory (where the script is located)
current_directory = os.path.dirname(os.path.realpath(__file__))
print("Main directory:", current_directory)

# Checks/creates the Results folder in this directory
results_dir_path = os.path.join(current_directory, "Results")
if not os.path.exists(results_dir_path):
    os.makedirs(results_dir_path)

people_dir_path = os.path.join(current_directory, "People")
txt_files = []  # Initialize an empty list to store the full paths of .txt files

# Check if the People directory exists
if os.path.exists(people_dir_path) and os.path.isdir(people_dir_path):
    # List all files in the directory and sort them
    files = sorted(os.listdir(people_dir_path))
    # Append the full path of .txt files to the list
    for file in files:
        if file.endswith('.txt'):
            full_path = os.path.join(people_dir_path, file)
            txt_files.append(full_path)
else:
    print("The provided directory does not exist or is not a directory.")

print(txt_files)

for item in txt_files:
    print(item)
#print(txt_files)






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