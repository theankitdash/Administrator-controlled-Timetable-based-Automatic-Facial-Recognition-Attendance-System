from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
import pandas as pd
from glob import glob

class Attendance_Calculation:
    def __init__(self, root):
        self.root=root
        self.root.geometry("700x400+0+0")
        self.root.title("Attendance Calculation")

        self.var_subcode=StringVar()

        #Bg Image
        img=Image.open(r"D:\Projects\SDP\iter.png")
        img=img.resize((700,400),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        BgImage = Label(self.root, image=self.photoimg)
        BgImage.place(x=0,y=0,width=700,height=400)

        title = Label(BgImage, text="VIEW ATTENDANCE", font=("Times new roman", 25,"bold"),bg="white")
        title.place(x=0,y=0,width=700,height=45)

        conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@4009', database='attendance-system')
        cursor = conn.cursor()
        cursor.execute("select distinct SUBCODE FROM schedule")
        subcode_li = [row[0] for row in cursor]
        subcode_li.insert(0, 'Select Subject Code')

        subcode_combo=ttk.Combobox(BgImage, values=subcode_li,textvariable=self.var_subcode,font=("times new roman",25,"bold"), state="readonly")
        subcode_combo.current(0)
        subcode_combo.place(x=150,y=100,width=350,height=70)

        bt=Button(BgImage,text="VIEW ATTENDANCE",command=self.calculate_attendance,cursor="hand2",font=("times new roman",25,"bold"),bg="darkgreen",fg="white")
        bt.place(x=150,y=200,width=350,height=70)

    def calculate_attendance(self): 
        Subject = self.var_subcode.get()
        if Subject=="":
            message.showinfo('Please enter the Subject Code')    
        os.chdir(
            f"D:\\Projects\\SDP\\Subjects\\{Subject}"
        )
        filenames = glob(
            f"D:\\Projects\\SDP\\Subjects\\{Subject}\\{Subject}*.csv"
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
        cs = f"D:\\Projects\\SDP\\Subjects\\{Subject}\\attendance.csv"
        with open(cs) as file:
            reader = csv.reader(file)
            r = 0

            for col in reader:
                c = 0
                for row in col:

                    label = Label(root, width=10, height=1, fg="black", font=("times", 15, " bold "), bg="white",text=row, relief=RIDGE)
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
        print(newdf) 

if __name__ == "__main__":
    root=Tk()  
    obj=Attendance_Calculation(root)
    root.mainloop()             