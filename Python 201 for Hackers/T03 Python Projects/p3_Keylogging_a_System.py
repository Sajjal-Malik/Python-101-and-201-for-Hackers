"""
====================================================
ETHICAL KEYBOARD EVENT LOGGING (EDUCATIONAL SCRIPT)
====================================================

Purpose:
---------
This script demonstrates how keyboard input can be
captured inside an application window using Python.

This helps ethical hackers understand:
- How keylogging logic works
- How events are captured
- How logs are stored
WITHOUT creating spyware or malware.

Scope:
------
✔ Only captures keys pressed inside this window
✖ No system-wide logging
✖ No background execution
✖ No persistence

Author:
-------
Educational / Ethical Hacking Learning Script
"""

# -------------------------------
# Import required standard modules
# -------------------------------

import tkinter as tk           # GUI framework (safe, application-scoped)
from datetime import datetime  # Used for timestamps
import os                      # File handling (safe logging)

# -------------------------------
# Configuration Section
# -------------------------------

# Log file name (stored in same directory as script)
LOG_FILE_NAME = "ethical_key_log.txt"

# -------------------------------
# Utility Function: Write to File
# -------------------------------


def write_log_to_file(log_message):
    """
    Writes a single log entry to the log file.

    Parameters:
    ----------
    log_message : str
        The formatted log entry to store.
    """

    # Open file in append mode (creates file if it doesn't exist)
    with open(LOG_FILE_NAME, "a", encoding="utf-8") as log_file:
        log_file.write(log_message + "\n")

# -----------------------------------------
# Keyboard Event Handler (Core Logic)
# -----------------------------------------


def handle_key_press(event):
    """
    This function is automatically called
    whenever a key is pressed inside the app window.

    'event' object contains detailed information
    about the key press.
    """

    # Current timestamp for logging
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # event.keysym  -> Human-readable key name (e.g., 'a', 'Return', 'Shift')
    # event.char    -> Actual character typed (empty for special keys)

    # Check if the key is a printable character
    if event.char.isprintable() and event.char != "":
        key_description = f"CHARACTER KEY: '{event.char}'"
    else:
        key_description = f"SPECIAL KEY: [{event.keysym}]"

    # Construct the final log entry
    log_entry = f"[{timestamp}] {key_description}"

    # Print to terminal (for learning visibility)
    print(log_entry)

    # Write to file (simulates how keyloggers store data)
    write_log_to_file(log_entry)

# -----------------------------------------
# GUI Application Setup
# -----------------------------------------


# Create the main application window
app = tk.Tk()

# Window title
app.title("Ethical Key Event Logger (Learning Demo)")

# Set window size
app.geometry("500x300")

# -------------------------------
# UI Components
# -------------------------------

# Instruction label
instruction_label = tk.Label(
    app,
    text=(
        "ETHICAL KEYBOARD EVENT LOGGER\n\n"
        "• This program logs keys ONLY inside this window\n"
        "• Logs are saved to: ethical_key_log.txt\n"
        "• This is for EDUCATIONAL purposes only\n\n"
        "Click here and start typing..."
    ),
    font=("Arial", 11),
    justify="center"
)

instruction_label.pack(pady=20)

# -------------------------------
# Event Binding
# -------------------------------

"""
Bind the KeyPress event to our handler.

<KeyPress> means:
- Every key pressed
- Only while this window is active
"""
app.bind("<KeyPress>", handle_key_press)

# -----------------------------------------
# Start the Event Loop
# -----------------------------------------

"""
This keeps the window open and listens
for keyboard events.
"""
app.mainloop()
