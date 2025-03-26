# File Name : Image.py
# Student Name: Asfia Siddiqui
# email: siddiqaf@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  3/26/25
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This is out first group project in this course and we used Github.
# Brief Description of what this module does: This code displays an image of Zubat
# Citations: chatgpt
# Anything else that's relevant:

from PIL import Image, ImageTk 
import tkinter as tk
import os

def display_image(image_path):
    """
    Displays the given image in a Tkinter window.
    @param image_path: str - The file path of the image to be displayed.
    @return: None
    """
    if not os.path.exists(image_path):
        print(f"Error: Image '{image_path}' not found.")
        return
    
    root = tk.Tk()
    root.title("Zubat Image")

    img = Image.open(image_path)
    img_tk = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=img_tk)
    label.pack()

    root.mainloop()

