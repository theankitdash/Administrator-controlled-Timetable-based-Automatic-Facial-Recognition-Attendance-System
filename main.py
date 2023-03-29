from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student_Registration
from faculty import Faculty_Registration
from subjects import Subject
from time_table import Time_Schedule
from take_attendance import Attendance_Registration
from view_attendance import Attendance_Calculation

class Attendance_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1080x720+0+0")
        self.root.title("Attendance Software")

        #Bg Image
        img=Image.open(r"D:\Projects\SDP\iter.png")
        img=img.resize((1080,720),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        BgImage = Label(self.root, image=self.photoimg)
        BgImage.place(x=0,y=0,width=1080,height=720)

        title = Label(BgImage, text="ATTENDANCE SYSTEM", font=("Times new roman", 25,"bold"),bg="white")
        title.place(x=0,y=0,width=1080,height=45)
        
        #Student Button
        Student_Reg = Image.open(r"D:\Projects\SDP\Student-Reg.png")
        Student_Reg = Student_Reg.resize((250,250), Image.ANTIALIAS)
        self.photoStudent_Reg=ImageTk.PhotoImage(Student_Reg)

        bt = Button(BgImage,image=self.photoStudent_Reg, command=self.student_details, cursor="hand2")
        bt.place(x=10,y=70,width=250,height=250)

        bt_1 = Button(BgImage, text= "Student Registration",command=self.student_details, cursor="hand2",font=("times new roman",18,"bold"),fg="blue", bg="white")
        bt_1.place(x=10,y=320, width=250, height=40)

        #Faculty Button
        Faculty_Reg = Image.open(r"D:\Projects\SDP\teacher.png")
        Faculty_Reg = Faculty_Reg.resize((250,250), Image.ANTIALIAS)
        self.photoFaculty_Reg=ImageTk.PhotoImage(Faculty_Reg)

        bt = Button(BgImage,image=self.photoFaculty_Reg, command=self.faculty_details, cursor="hand2")
        bt.place(x=400,y=70,width=250,height=250)

        bt_1 = Button(BgImage, text= "Faculty Registration",command=self.faculty_details, cursor="hand2",font=("times new roman",18,"bold"),fg="blue", bg="white")
        bt_1.place(x=400,y=320, width=250, height=40)

        #Subject Button
        Subject_Reg = Image.open(r"D:\Projects\SDP\subject.jpg")
        Subject_Reg = Subject_Reg.resize((250,250), Image.ANTIALIAS)
        self.photoSubject_Reg=ImageTk.PhotoImage(Subject_Reg)

        bt = Button(BgImage,image=self.photoSubject_Reg, command=self.subject_details, cursor="hand2")
        bt.place(x=800,y=70,width=250,height=250)

        bt_1 = Button(BgImage, text= "Subjects",command=self.subject_details, cursor="hand2",font=("times new roman",18,"bold"),fg="blue", bg="white")
        bt_1.place(x=800,y=320, width=250, height=40)

        #Time Table
        TimeTb = Image.open(r"D:\Projects\SDP\timetable.jpg")
        TimeTb = TimeTb.resize((250,250), Image.ANTIALIAS)
        self.photoTimeTb=ImageTk.PhotoImage(TimeTb)

        TimeTb_bt = Button(BgImage,image=self.photoTimeTb, command=self.time_table,cursor="hand2")
        TimeTb_bt.place(x=10,y=400,width=250,height=250)

        TimeTb_bt_1 = Button(BgImage, text= "Time Table", command=self.time_table,cursor="hand2",font=("times new roman",18,"bold"),fg="blue", bg="white")
        TimeTb_bt_1.place(x=10,y=650, width=250, height=40)


        #Attendance Registration
        Attendance_Det = Image.open(r"D:\Projects\SDP\take-att.jpg")
        Attendance_Det = Attendance_Det.resize((250,250), Image.ANTIALIAS)
        self.photoAttendance_Det=ImageTk.PhotoImage(Attendance_Det)

        bt = Button(BgImage,image=self.photoAttendance_Det, command=self.recognize_attendance,cursor="hand2")
        bt.place(x=400,y=400,width=250,height=250)

        bt_1 = Button(BgImage, text= "Take Attendance", command=self.recognize_attendance,cursor="hand2",font=("times new roman",18,"bold"),fg="blue", bg="white")
        bt_1.place(x=400,y=650, width=250, height=40)

        #Calculate Attendance
        Attendance_cal = Image.open(r"D:\Projects\SDP\atten.jpg")
        Attendance_cal = Attendance_cal.resize((250,250), Image.ANTIALIAS)
        self.photoAttendance_cal=ImageTk.PhotoImage(Attendance_cal)

        bt = Button(BgImage,image=self.photoAttendance_cal, command=self.attendance_calculate,cursor="hand2")
        bt.place(x=800,y=400,width=250,height=250)

        bt_1 = Button(BgImage, text= "View Attendance", command=self.attendance_calculate,cursor="hand2",font=("times new roman",18,"bold"),fg="blue", bg="white")
        bt_1.place(x=800,y=650, width=250, height=40)


    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Registration(self.new_window)

    def faculty_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Faculty_Registration(self.new_window)

    def subject_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Subject(self.new_window) 

    def time_table(self):
        self.new_window=Toplevel(self.root)
        self.app=Time_Schedule(self.new_window)       

    def recognize_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_Registration(self.new_window) 

    def attendance_calculate(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_Calculation(self.new_window)    

         


if __name__ == "__main__":
    root=Tk()  
    obj=Attendance_System(root)
    root.mainloop()        