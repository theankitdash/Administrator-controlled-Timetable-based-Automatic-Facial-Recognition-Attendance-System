import cv2
import os
import numpy as np
import time
import datetime
import schedule

trainedimages = ("classifier.xml")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
attendance_path = "C:\\Users\\ankit\\Desktop\\New folder\\Subjects"

class Attendance_Registration:
    def period1(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system', charset='utf8')
        my_cursor = conn.cursor()
        cursor.execute("select SUBCODE from schedule where ID='B11'")
        sub = cursor.fetchone()

        subject = "".join(map(str, sub))
        schedule.every().day.at("09:00").do(FillAttendance)

    def FillAttendance(self):
        sub = self.var_Sub.get()
        now = time.time()
        future = now + 7

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(trainedimages)

        faceCascade = cv2.CascadeClassifier(harcascadePath)   
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
                        
                if confidence>60:
                    global Subject
                    global aa
                    global date
                    global timeStamp
                    Subject = self.var_Sub.get()
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
                    cv2.putText(im,f"Semester:{i}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(im,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(im,f"Branch:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)           
                else:
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(im,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            if time.time() > future:
                break

            attendance = attendance.drop_duplicates(["Roll No"], keep="first")
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


        cam.release()
        cv2.destroyAllWindows()
    
if __name__ == "__main__":
    root=Tk()  
    obj=Attendance_Registration(root)
    root.mainloop()                            