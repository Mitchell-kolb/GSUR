
from chrome_automation import automation as chrome_setup, test_selenium
from djc_barmaker import setup as djc_setup

import os
import platform

def clear_screen():
    # Clear the command line screen.
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def main_menu():
    while True:
        clear_screen()
        print("\nMain Menu")
        print("1. Test Selenium")
        print("2. Download Files")
        print("3. Analyze Files")
        print("4. Exit")
        
        choice = input("Please enter your choice (1-4): ")

        if choice == '1':
            test_selenium()
            input("Press Enter to return to the main menu...")
        elif choice == '2':
            download_files()
            input("Press Enter to return to the main menu...")
        elif choice == '3':
            djc_setup()
            input("Press Enter to return to the main menu...")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")


def download_files():
    while True:
        num = input("How many files do you want to download? (1-2000 or 'all'): ")
        if num.isdigit() and 1 <= int(num) <= 2000:
            print(f"Downloading {num} files...")
            chrome_setup()
            break
        elif num.lower() == 'all':
            print("Downloading all files...")
            chrome_setup()
            break
        else:
            print("Invalid input. Please enter a number between 1 and 2000, or type 'all'.")


if __name__ == "__main__":
    main_menu()
