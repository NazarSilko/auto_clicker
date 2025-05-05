import pyautogui
import keyboard
import threading
import time

# Get screen size and calculate center coordinates
screen_width, screen_height = pyautogui.size()
x, y = screen_width // 2, screen_height // 2  # Center of the screen

# Clicker settings
delay = 0.01  # Delay between clicks in seconds
clicking = False  # Flag to track if the clicker is active

# Function that performs clicking while the flag is True
def clicker():
    global clicking
    while True:
        if clicking:
            pyautogui.click(x, y)
            time.sleep(delay)
        else:
            time.sleep(0.1)

# Start the clicker thread
threading.Thread(target=clicker, daemon=True).start()

print(f"Screen size: {screen_width}x{screen_height}")
print(f"Clicking at screen center: ({x}, {y})")
print("Press F8 to toggle the clicker on/off.")
print("Press ESC to exit the program.")

# Listen for keyboard input to toggle clicking or exit
while True:
    try:
        if keyboard.is_pressed('F8'):
            clicking = not clicking
            state = "ON" if clicking else "OFF"
            print(f"Clicker: {state}")
            time.sleep(0.5)  # Prevent multiple toggles from one press

        elif keyboard.is_pressed('esc'):
            print("Exiting the program.")
            break
    except:
        break

