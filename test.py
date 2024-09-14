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

trainedimages = ("classifier.xml")
face_cascade = 'haarcascade_frontalface_default.xml'
attendance_path = "D:\\Projects\\SDP\\Subjects"

class Attendance_Registration:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Attendance Registration")

        #Bg Image
        img=Image.open(r"D:\Projects\SDP\itersoa.jpg")
        img=img.resize((1280,720),Image.Resampling.LANCZOS)
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
            ___, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
                    date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                    aa = df.loc[df["Roll No"] == Id]["Name"].values
                    global tt
                    tt = str(Id) + "-" + aa
                    
                    attendance.loc[len(attendance)] = [
                        Id,
                        aa,
                    ]
                    
                    str_id = str(Id)
                    str_name = str(aa)
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img, f"Roll No:{str_id}", (x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Name:{str_name}", (x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)        
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

            attendance = attendance.drop_duplicates(["Roll No"], keep="first")
            cv2.imshow("Filling Attendance...", img)
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

            day_number = datetime.datetime.fromtimestamp(ts).strftime("%w")
            weekday = int(day_number)

            conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@4009', database='attendance-system')
            cursor = conn.cursor()
            cursor.execute("select distinct Branch FROM student where Roll_No = %s", (str_id,))
            result = cursor.fetchone()

            query = "select SUBCODE from schedule where DAYID= %s AND PERIODID = %s AND BRANCH = %s" 
            cursor.execute(query, (weekday, period, result[0],))
            result1 = cursor.fetchall()
            result_str = ""

            for row in result1:
                result_str += str(row[0]) + ", "
            print(result_str[:-2])     
            
            path = os.path.join(attendance_path, result_str[:-2])
            isExist = os.path.exists(path)

            def save_attendance():    
                fileName = (f"{path}/" + result_str[:-2] + "_" + date+ "_" + Hour + "-" + Minute + "-" + Second + ".csv")
                attendance1 = attendance.drop_duplicates(["Roll No"], keep="first")
                print(attendance1)
                attendance1.to_csv(fileName, index=False)

            
            if isExist:
                save_attendance()
            else:
                os.mkdir(path) 
                save_attendance()
                
        period_names = list(map(lambda x: str(x), range(1, 5+1)))

        # Within the 9:00 AM - 9:10 AM interval
        if datetime.time(9, 0) <= now < datetime.time(9, 10):
            period = period_names[0]
            time_attendance()

        # Within the 10:00 AM - 10:10 AM interval
        elif datetime.time(10, 00) <= now < datetime.time(10, 10): 
            period = period_names[1]
            time_attendance()

        # Within the 11:00 AM - 11:10 AM interval
        elif datetime.time(11, 00) <= now < datetime.time(15, 10): 
            period = period_names[2]
            time_attendance()

        # Within the 12:00 PM - 12:10 PM interval
        elif datetime.time(12, 00) <= now < datetime.time(12, 10):  
            period = period_names[3]
            time_attendance()
            
        # Within the 1:00 PM - 1:10 PM interval
        elif datetime.time(13, 00) <= now < datetime.time(13, 10): 
            period = period_names[4]
            time_attendance()

        else:
            print("You are late")              
        cam.release()
        cv2.destroyAllWindows()

    
if __name__ == "__main__":
    root=Tk()  
    obj=Attendance_Registration(root)
    root.mainloop()   