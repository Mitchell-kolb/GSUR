import customtkinter
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("GSUR Automation")
        #self.geometry("950x450")

        # Calculate window position to center the GUI in the middle of the users screen dynamically
        window_width = 700
        window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)


        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "wsu_logo2.png")), size=(40, 40))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "test-dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "test-light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "login-dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "login-light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "download-dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "download-light.png")), size=(20, 20))
        self.analyze_files_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "analyze-dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "analyze-light.png")), size=(20, 20))
        self.settings_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "settings-dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "settings-light.png")), size=(20, 20))

        # create navigation frame or LEFT SIDEBAR
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  GSUR", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.test_selenium_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Test Selenium",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.test_selenium_button_event)
        self.test_selenium_button.grid(row=1, column=0, sticky="ew")

        self.edit_login_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Edit Login",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.edit_login_button_event)
        self.edit_login_button.grid(row=2, column=0, sticky="ew")

        self.download_files_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Download Files",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.download_files_button_event)
        self.download_files_button.grid(row=3, column=0, sticky="ew")

        self.analyze_files_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Analyze Files",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.analyze_files_image, anchor="w", command=self.analyze_files_button_event)
        self.analyze_files_button.grid(row=4, column=0, sticky="ew")

        self.settings_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Settings",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.settings_image, anchor="w", command=self.settings_button_event)
        self.settings_button.grid(row=5, column=0, sticky="ew")

        
        # Adjust the appearance_mode_menu to reflect the system's theme
        current_appearance_mode = customtkinter.get_appearance_mode()  # Get the current appearance mode
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event, text_color=("gray10", "gray90"), fg_color=("gray70", "gray10"), button_color=("gray70", "gray10"), button_hover_color=("gray50", "gray30"), dropdown_fg_color=("gray90", "gray10"), dropdown_hover_color=("gray70", "gray30"))
        self.appearance_mode_menu.set(current_appearance_mode)  # Set the menu to show the current appearance mode
        self.appearance_mode_menu.grid(row=7, column=0, padx=20, pady=20, sticky="s")


        # create test selenium frame or RIGHT 3/4 of screen
        self.test_selenium_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.test_selenium_frame.grid_columnconfigure(0, weight=1)

        self.test_selenium_frame_large_image_label = customtkinter.CTkLabel(self.test_selenium_frame, text="", image=self.large_test_image)
        self.test_selenium_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.test_selenium_frame_button_1 = customtkinter.CTkButton(self.test_selenium_frame, text="", image=self.image_icon_image)
        self.test_selenium_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.test_selenium_frame_button_2 = customtkinter.CTkButton(self.test_selenium_frame, text="CTkButton1", image=self.image_icon_image, compound="right")
        self.test_selenium_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.test_selenium_frame_button_3 = customtkinter.CTkButton(self.test_selenium_frame, text="CTkButton2", image=self.image_icon_image, compound="top")
        self.test_selenium_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.test_selenium_frame_button_4 = customtkinter.CTkButton(self.test_selenium_frame, text="CTkButton3", image=self.image_icon_image, compound="bottom", anchor="w")
        self.test_selenium_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create Edit login frame
        self.edit_login_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.edit_login_frame.grid_columnconfigure(0, weight=1)
        self.edit_login_frame_button_5 = customtkinter.CTkButton(self.edit_login_frame, text="CTkButton5 ahhh", image=self.image_icon_image, compound="right")
        self.edit_login_frame_button_5.grid(row=2, column=0, padx=20, pady=10)

        # create Download frame
        self.download_files_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.download_files_frame.grid_columnconfigure(0, weight=1)
        self.download_files_frame_button_6 = customtkinter.CTkButton(self.download_files_frame, text="CTkButton6 ahhh", image=self.image_icon_image, compound="right")
        self.download_files_frame_button_6.grid(row=2, column=0, padx=20, pady=10)

        # create Analzye frame
        self.analyze_files_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.analyze_files_frame.grid_columnconfigure(0, weight=1)
        self.analyze_files_frame_button_7 = customtkinter.CTkButton(self.analyze_files_frame, text="CTkButton7 ahhh", image=self.image_icon_image, compound="right")
        self.analyze_files_frame_button_7.grid(row=2, column=0, padx=20, pady=10)

        # create Settings frame
        self.settings_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.settings_frame.grid_columnconfigure(0, weight=1)
        self.settings_frame_button_8 = customtkinter.CTkButton(self.settings_frame, text="CTkButton8 ahhh", image=self.image_icon_image, compound="right")
        self.settings_frame_button_8.grid(row=2, column=0, padx=20, pady=10)


        # select default frame
        self.select_frame_by_name("Test Selenium")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.test_selenium_button.configure(fg_color=("gray75", "gray25") if name == "Test Selenium" else "transparent")
        self.edit_login_button.configure(fg_color=("gray75", "gray25") if name == "Edit Login" else "transparent")
        self.download_files_button.configure(fg_color=("gray75", "gray25") if name == "Download Files" else "transparent")
        self.analyze_files_button.configure(fg_color=("gray75", "gray25") if name == "Analyze Files" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "Settings" else "transparent")


        # show selected frame
        if name == "Test Selenium":
            self.test_selenium_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.test_selenium_frame.grid_forget()
        if name == "Edit Login":
            self.edit_login_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.edit_login_frame.grid_forget()
        if name == "Download Files":
            self.download_files_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.download_files_frame.grid_forget()
        if name == "Analyze Files":
            self.analyze_files_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.analyze_files_frame.grid_forget()
        if name == "Settings":
            self.settings_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.settings_frame.grid_forget()

    def test_selenium_button_event(self):
        self.select_frame_by_name("Test Selenium")

    def edit_login_button_event(self):
        self.select_frame_by_name("Edit Login")

    def download_files_button_event(self):
        self.select_frame_by_name("Download Files")

    def analyze_files_button_event(self):
        self.select_frame_by_name("Analyze Files")

    def settings_button_event(self):
        self.select_frame_by_name("Settings")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()

