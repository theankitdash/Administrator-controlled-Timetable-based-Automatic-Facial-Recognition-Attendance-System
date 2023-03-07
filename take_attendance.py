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
face_cascade = 'haarcascade_frontalface_default.xml'
attendance_path = "C:\\Users\\ankit\\Desktop\\New folder\\Roll"

class Attendance_Registration:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Attendance Registration")

        self.var_roll=StringVar()

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
        now = datetime.datetime.now().time()

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(trainedimages)

        faceCascade = cv2.CascadeClassifier(face_cascade)   
        df = pd.read_csv("studentdetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ["Roll No", "Name"]
        attendance = pd.DataFrame(columns=col_names)

        while True:
            ___, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                global Id
                Id, predict = recognizer.predict(gray[y : y + h, x : x + w])
                confidence=int((100*(1-predict/300)))
                        
                if confidence>70:
                    global aa
                    global date
                    global timeStamp
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime(
                        "%Y-%m-%d"
                    )
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime(
                        "%H:%M:%S"
                    )
                    aa = df.loc[df["Roll No"] == Id]["Name"].values
                    global tt
                    tt = str(Id) + "-" + aa
                    
                    attendance.loc[len(attendance)] = [
                        Id,
                        aa,
                    ]
                    str_id = str(Id)
                    str_name = str(aa)
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(im, f"Roll No:{str_id}", (x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(im, f"Name:{str_name}", (x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)        
                else:
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(im,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

            attendance = attendance.drop_duplicates(["Roll No"], keep="first")
            cv2.imshow("Filling Attendance...", im)
            key = cv2.waitKey(30)
            if key == ord('q'):
                break

        def time_attendance():
            ts = time.time()
            global date    
            attendance[date] = 1
            date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
            timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
            Hour, Minute, Second = timeStamp.split(":")

            str_id = str(Id)
            path = os.path.join(attendance_path, str_id)
            isExist = os.path.exists(path)
            
            def save_attendance():    
                fileName = (f"{path}/"+ str_id+ "_" + date+ "_" + Hour + "-" + Minute + "-" + Second + ".csv")
                attendance1 = attendance.drop_duplicates(["Roll No"], keep="first")
                print(attendance1)
                attendance1.to_csv(fileName, index=False)

            if isExist:
                save_attendance()
            else:
                os.mkdir(path) 
                save_attendance()
                
        #Within the 9:00 AM - 9:10 AM interval
        if datetime.time(9, 0) <= now < datetime.time(9, 10):
           time_attendance()
    
        #Within the 10:00 AM - 10:10 AM interval
        elif datetime.time(10, 00) <= now < datetime.time(10, 10): 
            time_attendance()
            
        #Within the 11:00 AM - 11:10 AM interval
        elif datetime.time(11, 00) <= now < datetime.time(11, 10): 
            time_attendance()          

        #Within the 12:00 PM - 12:10 PM interval
        elif datetime.time(12, 00) <= now < datetime.time(12, 10):  
            time_attendance()
            
        #Within the 1:00 PM - 1:10 PM interval
        elif datetime.time(13, 00) <= now < datetime.time(13, 10): 
            time_attendance()
        else:
            print("You are late")              
        cam.release()
        cv2.destroyAllWindows()

    
if __name__ == "__main__":
    root=Tk()  
    obj=Attendance_Registration(root)
    root.mainloop()   