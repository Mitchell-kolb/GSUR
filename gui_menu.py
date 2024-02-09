
#Side bar GUI

import customtkinter as ctk

ctk.set_appearance_mode("System")  # or "Dark", "Light"
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title('CustomTkinter Frames Example')
app.geometry('800x500')

# Main Frame Layout
sidebar_frame = ctk.CTkFrame(master=app, width=200, corner_radius=0, fg_color=("gray75", "gray30"))
sidebar_frame.pack(side='left', fill='y')

main_frame = ctk.CTkFrame(master=app, corner_radius=0)
main_frame.pack(side='right', fill='both', expand=True)

# Sidebar Buttons
def change_content(content):
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    if content == "Setup":
        label = ctk.CTkLabel(main_frame, text="Setup Content", fg_color=("gray75", "gray30"))
        label.pack(pady=20)
    elif content == "Test Browser":
        button = ctk.CTkButton(main_frame, text="Test Browser Action", fg_color=("gray75", "gray30"))
        button.pack(pady=20)
    elif content == "Download Files":
        entry = ctk.CTkEntry(main_frame, placeholder_text="Download Path")
        entry.pack(pady=20)
    elif content == "Analyze Files":
        slider = ctk.CTkSlider(main_frame, from_=0, to=100)
        slider.pack(pady=20)

button_setup = ctk.CTkButton(sidebar_frame, text="Setup", command=lambda: change_content("Setup"))
button_setup.pack(pady=10)

button_test_browser = ctk.CTkButton(sidebar_frame, text="Test Browser", command=lambda: change_content("Test Browser"))
button_test_browser.pack(pady=10)

button_download_files = ctk.CTkButton(sidebar_frame, text="Download Files", command=lambda: change_content("Download Files"))
button_download_files.pack(pady=10)

button_analyze_files = ctk.CTkButton(sidebar_frame, text="Analyze Files", command=lambda: change_content("Analyze Files"))
button_analyze_files.pack(pady=10)

# Initial Content
change_content("Setup")

app.mainloop()