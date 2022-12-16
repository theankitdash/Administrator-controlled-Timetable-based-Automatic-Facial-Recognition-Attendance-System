from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
import numpy as np
import pandas as pd
import time
import datetime
from glob import glob

class show_attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("500x700+0+0")
        self.root.title("Attendance Registration")

        self.var_Sub=StringVar()

        #Bg Image
        img=Image.open(r"C:\Users\ankit\Desktop\New folder\itersoa.jpg")
        img=img.resize((500,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        BgImage = Label(self.root, image=self.photoimg)
        BgImage.place(x=0,y=0,width=500,height=700)

        title = Label(BgImage, text="ATTENDANCE REGISTRATION", font=("Times new roman", 25,"bold"),bg="white")
        title.place(x=0,y=0,width=500,height=45)

        sub_label=Label(BgImage,text="Subject", font=("times new roman", 12,"bold"),bg="white")
        sub_label.place(x=130,y=150,width=200,height=40)

        sub_combo=ttk.Combobox(BgImage, textvariable=self.var_Sub, font=("times new roman",12,"bold"), state="readonly")
        sub_combo["values"]=("Select Subject", "PSAD-2", "UHV", "ESPUA", "PSH", "PSM", "ECES")
        sub_combo.current(0)
        sub_combo.place(x=130,y=200,width=200,height=40)

        bt=Button(BgImage,text="VIEW ATTENDANCE",command=self.calculate_attendance,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        bt.place(x=130,y=250,width=200,height=40)

    def calculate_attendance(self):
        Subject = self.var_Sub.get()
        if Subject=="":
            message.showinfo('Please enter the subject name.')
            
        os.chdir(
            f"C:\\Users\\ankit\\Desktop\\New folder\\Subjects\\{Subject}"
        )
        filenames = glob(
            f"C:\\Users\\ankit\\Desktop\\New folder\\Subjects\\{Subject}\\{Subject}*.csv"
        )

        df = [pd.read_csv(f) for f in filenames]
        newdf = df[0]
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")
        newdf.fillna(0, inplace=True)

        newdf["Attendance"] = 0
        for i in range(len(newdf)):
            newdf["Attendance"].iloc[i] = str(int(round(newdf.iloc[i, 2:-1].mean() * 100)))+'%'
            
        newdf.to_csv("attendance.csv", index=False)

        root = Tk()
        root.title("Attendance of "+Subject)
        root.configure(background="black")
        cs = f"C:\\Users\\ankit\\Desktop\\New folder\\Subjects\\{Subject}\\attendance.csv"
        with open(cs) as file:
            reader = csv.reader(file)
            r = 0

            for col in reader:
                c = 0
                for row in col:

                    label = Label(root, width=10, height=1, fg="yellow", font=("times", 15, " bold "), bg="black",text=row, relief=RIDGE)
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
        print(newdf)

if __name__ == "__main__":
    root=Tk()  
    obj=show_attendance(root)
    root.mainloop()     