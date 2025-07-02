# This code runs in Replit using the virtual display
import pyautogui
import time
import os

# Set up the display for the virtual environment
os.environ['DISPLAY'] = ':0'

# Disable pyautogui failsafe for headless environment
pyautogui.FAILSAFE = False

print("Starting mouse automation script...")

# Give a moment for setup
time.sleep(2)

# Get the screen resolution
screenWidth, screenHeight = pyautogui.size()
print(f"Screen size: {screenWidth}x{screenHeight}")

# Move the mouse to different positions
positions = [
    (100, 100),
    (screenWidth - 100, 100),
    (screenWidth - 100, screenHeight - 100),
    (100, screenHeight - 100),
    (screenWidth // 2, screenHeight // 2)
]

for i, (x, y) in enumerate(positions):
    print(f"Moving to position {i+1}: ({x}, {y})")
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()
    time.sleep(0.5)

print("Mouse automation complete!")

# Keep the script running for a moment
time.sleep(2)
