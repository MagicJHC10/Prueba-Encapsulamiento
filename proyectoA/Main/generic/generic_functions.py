import os
from pynput.mouse import Button, Controller as MouseController

def change_directory():
    # Print the directory of this .py file
    print(f"The current script is located at: {os.path.abspath(__file__)}")
    
    # Move two levels back in the directory structure
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)  
    os.chdir(parent_directory)
    
    print(f"Changed directory to: {os.getcwd()}")

def move_mouse_to(x, y):

    mouse = MouseController()
    mouse.position = (x, y)