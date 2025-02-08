import time
import winsound
import customtkinter as ctk
from tkinter import StringVar

# Initialize UI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")
root = ctk.CTk()
root.title("Workout Timer")
root.geometry("400x450")

# Font setup
FONT_NAME = "Jockey One"

# Variables
set_count = StringVar()
time_sec = StringVar()
rest_sec = StringVar()
current_set = 0
running = False

def countdown_timer(seconds, label, callback):
    def update():
        nonlocal seconds  # Ensure 'seconds' is used correctly inside nested function
        global running
        if running and seconds >= 0:
            label.configure(text=f"{seconds:02}")
            root.after(1000, update)
            seconds -= 1  # Reduce time
        elif running and seconds < 0:
            winsound.Beep(1000, 500)
            callback()

    update()

# Start Workout
def start_workout():
    global current_set, running
    if running:
        return
    running = True
    current_set = 1
    run_set()

# Stop Timer
def stop_timer():
    global running
    running = False

# Reset Timer
def reset_timer():
    global running, current_set
    running = False
    current_set = 0
    set_label.configure(text="00")
    time_label.configure(text="00")

# Run Each Set
def run_set():
    global current_set
    if current_set <= int(set_count.get()):
        set_label.configure(text=f"{current_set}")
        countdown_timer(int(time_sec.get()), time_label, start_rest)
    else:
        reset_timer()

# Rest Period
def start_rest():
    countdown_timer(int(rest_sec.get()), time_label, next_set)

# Next Set
def next_set():
    global current_set
    current_set += 1
    run_set()

# Font name
FONT_NAME = "Jockey One"

# Title
ctk.CTkLabel(root, text="Countdown!", font=(FONT_NAME, 24)).grid(row=0, column=0, pady=20, columnspan=2)

# Frame for the time display labels
frame = ctk.CTkFrame(root)
frame.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

set_label = ctk.CTkLabel(frame, text="00", font=(FONT_NAME, 32), width=150)
set_label.grid(row=0, column=0, padx=10, sticky="ew")

time_label = ctk.CTkLabel(frame, text="00", font=(FONT_NAME, 32), width=300)
time_label.grid(row=0, column=1, padx=5, sticky="ew")

# Configure grid columns for the root window
root.grid_columnconfigure(0, weight=1, minsize=150)
root.grid_columnconfigure(1, weight=2, minsize=150)

# Set up input fields and labels
ctk.CTkLabel(root, text="Set Count:", font=(FONT_NAME, 16)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
ctk.CTkEntry(root, textvariable=set_count).grid(row=2, column=1, padx=5, pady=10, sticky="ew")

ctk.CTkLabel(root, text="Time (sec):", font=(FONT_NAME, 16)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
ctk.CTkEntry(root, textvariable=time_sec).grid(row=3, column=1, padx=5, pady=10, sticky="ew")

ctk.CTkLabel(root, text="Rest (sec):", font=(FONT_NAME, 16)).grid(row=4, column=0, padx=10, pady=10, sticky="w")
ctk.CTkEntry(root, textvariable=rest_sec).grid(row=4, column=1, padx=5, pady=10, sticky="ew")

# Buttons frame
button_frame = ctk.CTkFrame(root)
button_frame.grid(row=5, column=0, columnspan=2, pady=20, sticky="ew")
# Set fixed width for buttons to make them narrower
button_width = 115  # Adjust this value as needed

ctk.CTkButton(button_frame, text="Start", command=start_workout, font=(FONT_NAME, 16), width=button_width).grid(row=0, column=0, padx=10, pady=10)
ctk.CTkButton(button_frame, text="Stop", command=stop_timer, font=(FONT_NAME, 16), width=button_width).grid(row=0, column=1, padx=10, pady=10)
ctk.CTkButton(button_frame, text="Reset", command=reset_timer, font=(FONT_NAME, 16), width=button_width).grid(row=0, column=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
