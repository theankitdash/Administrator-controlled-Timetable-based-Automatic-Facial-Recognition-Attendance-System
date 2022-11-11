from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Attendance_Registration:
    def __init__(self, root):
        self.root=root
        self.root.geometry("500x700+0+0")
        self.root.title("Attendance Registration")

               


if __name__ == "__main__":
    root=Tk()  
    obj=Attendance_Registration(root)
    root.mainloop()                