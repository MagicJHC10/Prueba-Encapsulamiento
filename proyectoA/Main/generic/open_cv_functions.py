import cv2
from PIL import ImageGrab
from robot.libraries.BuiltIn import BuiltIn
from pynput.mouse import Button, Controller as MouseController
import numpy as np
import os

def click_on_image(image_path, fidelity=0.85):
    print(fidelity)
    fidelity = float(fidelity)
    print(image_path)
    # Load the reference image
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    # Convert the image to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Take a screenshot
    screenshot = ImageGrab.grab()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Convert the screenshot to grayscale
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Search for the reference image in the screenshot
    result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    print(max_val)
    # If the maximum value is greater than a threshold, we assume we found the image
    if max_val > fidelity:
        # Calculate the position of the center of the image
        center_x = max_loc[0] + image.shape[1] // 2
        center_y = max_loc[1] + image.shape[0] // 2

        # Click on the center of the image
        mouse = MouseController()
    
        # Move the cursor to the position (x, y)
        mouse.position = (center_x, center_y)
        mouse.press(Button.left)
        mouse.release(Button.left)
    else:
        BuiltIn().fail("Image not found on the screen.")   
        print("Image not found")

def find_image_color(image_path, precision=0.99):
    precision = float(precision)
    # Load the reference image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    print(os.path.abspath(image_path))
    # Ensure the reference image is in the correct format
    if image is None:
        print("Error: Could not load image at", image_path)
        return False
    if image.dtype != np.uint8:
        image = image.astype(np.uint8)

    # Take a screenshot
    screenshot = ImageGrab.grab()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Ensure the screenshot is in the correct format
    if screenshot.dtype != np.uint8:
        screenshot = screenshot.astype(np.uint8)

    # Ensure both images have the same number of channels (3 channels for BGR)
    if len(image.shape) != 3 or image.shape[2] != 3:
        print("Error: The reference image does not have 3 channels")
        return False
    if len(screenshot.shape) != 3 or screenshot.shape[2] != 3:
        print("Error: The screenshot does not have 3 channels")
        return False

    # Ensure both images have the same depth
    if image.dtype != screenshot.dtype:
        print("Error: The depth of the reference image and the screenshot do not match")
        return False

    # Search for the reference image in the screenshot
    result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print("La fidelidad es: ",max_val)
    

    # If the maximum value is greater than a threshold, we assume we found the image
    if max_val > precision:
        # Calculate the position of the center of the image
        center_x = max_loc[0] + image.shape[1] // 2
        center_y = max_loc[1] + image.shape[0] // 2

        # Return the coordinates of the center of the image
        print("Image found at:", center_x, center_y)
        return center_x, center_y
    else:
        print("Image not found")
        return False