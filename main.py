import time
import cv2
import numpy as np
import pyautogui
import keyboard

# Load the button template image
TEMPLATE_PATH = "button_template.png"
button_template = cv2.imread(TEMPLATE_PATH, cv2.IMREAD_UNCHANGED)

if button_template is None:
    raise ValueError("Button template image not found. Ensure the path is correct.")


# Function to find the button and click it
def find_and_click_button():
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    button_gray = cv2.cvtColor(button_template, cv2.COLOR_RGB2GRAY)
    result = cv2.matchTemplate(screenshot, button_gray, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.8:  # Confidence threshold
        button_x, button_y = max_loc
        button_x += button_template.shape[1] // 2
        button_y += button_template.shape[0] // 2

        pyautogui.click(button_x, button_y)
        print(f"Clicked button at: {button_x}, {button_y}")
    else:
        print("Button not found")


# Stop flag
running = True


def stop_script():
    global running
    running = False
    print("Script stopping...")


# Register the stop key
keyboard.add_hotkey("F9", stop_script)

# Main loop
time.sleep(3)  # Give time to switch to the app
print("Press F9 to stop the script.")
while running:
    find_and_click_button()
    time.sleep(8)  # Wait 8 seconds before clicking again
