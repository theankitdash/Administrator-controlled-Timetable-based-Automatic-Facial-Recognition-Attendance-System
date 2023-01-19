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

trainedimages = ("classifier.xml")
harcascadePath = "haarcascade_frontalface_default.xml"
attendance_path = "C:\\Users\\ankit\\Desktop\\Subjects\\Roll"

class Attendance_Registration:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Attendance Registration")

        self.var_Roll=StringVar()
        self.var_Sub=StringVar()
        

        #Bg Image
        img=Image.open(r"C:\Users\ankit\Desktop\New folder\itersoa.jpg")
        img=img.resize((1280,720),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        BgImage = Label(self.root, image=self.photoimg)
        BgImage.place(x=0,y=0,width=1280,height=720)

        title = Label(BgImage, text="ATTENDANCE REGISTRATION", font=("Times new roman", 25,"bold"),bg="white")
        title.place(x=0,y=0,width=1280,height=45)

        bt=Button(BgImage,text="RECOGNIZE",command=self.FillAttendance,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        bt.place(x=500,y=270,width=250,height=50)
    
    def FillAttendance(self):
        sub = self.var_Sub.get()
        now = time.time()
        future = now + 7

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(trainedimages)

        faceCascade = cv2.CascadeClassifier(harcascadePath)

        conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system', charset='utf8')   
        df = pd.read_sql("select SUBCODE FROM subjects",conn)
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ["Subject Code"]
        attendance = pd.DataFrame(columns=col_names)
        while True:
            ___, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                global Id

                Id, predict = recognizer.predict(gray[y : y + h, x : x + w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system', charset='utf8')
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Roll_No="+str(Id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Branch from student where Roll_No="+str(Id))
                d=my_cursor.fetchone()
                d="+".join(d)


                my_cursor.execute("select Semester from student where Roll_No="+str(Id))
                i=my_cursor.fetchone()
                i="+".join(i)
                        
                if confidence>50:
                    global Roll_
                    global aa
                    global date
                    global timeStamp
                    Roll_ = self.var_Roll.get()
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime(
                        "%Y-%m-%d"
                    )
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime(
                        "%H:%M:%S"
                    )
                    aa = df.loc[df["Roll_"] == Id]["Subject Code"].values
                    global tt
                    tt = str(Id) + "-" + aa
                    
                    attendance.loc[len(attendance)] = [
                        Id,
                        aa,
                    ]
                    cv2.putText(im,f"Semester:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(im,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(im,f"Branch:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)           
                else:
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(im,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            if time.time() > future:
                break

            attendance = attendance.drop_duplicates(["Roll_"], keep="first")
            cv2.imshow("Filling Attendance...", im)
            key = cv2.waitKey(30) & 0xFF
            if key == 27:
                break

        ts = time.time()
        print(aa)
        
        attendance[date] = 1
        date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        Hour, Minute, Second = timeStamp.split(":")
        
        path = os.path.join(attendance_path, Roll_)
        fileName = (
            f"{path}/"
            + Roll_
            + "_"
            + date
            + "_"
            + Hour
            + "-"
            + Minute
            + "-"
            + Second
            + ".csv"
        )
        attendance = attendance.drop_duplicates(["Roll_"], keep="first")
        print(attendance)
        attendance.to_csv(fileName, index=False)

        messagebox.showinfo("Congrats","Attendance marked successfully of " + Roll_)
        
        cam.release()
        cv2.destroyAllWindows()
    
if __name__ == "__main__":
    root=Tk()  
    obj=Attendance_Registration(root)
    root.mainloop()                            