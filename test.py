""" import os

# Get the current working directory (where the script is located)
current_directory = os.path.dirname(os.path.realpath(__file__))
print("Current directory:", current_directory)
# Checks/creates a the People folder in this directory.
dir_path = current_directory + "/People"
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
else:
    print("Already exists")
 """


