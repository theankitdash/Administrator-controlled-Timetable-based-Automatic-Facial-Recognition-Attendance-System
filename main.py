from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student_Registration
from attendance_reg import Attendance_Registration
from faculty import Faculty_Registration
from subjects import Subject
from time_table import Time_Schedule

class Attendance_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("Attendance Software")

        #Bg Image
        img=Image.open(r"C:\Users\ankit\Desktop\New folder\itersoa.jpg")
        img=img.resize((1280,720),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        BgImage = Label(self.root, image=self.photoimg)
        BgImage.place(x=0,y=0,width=1280,height=720)

        title = Label(BgImage, text="ATTENDANCE SYSTEM", font=("Times new roman", 25,"bold"),bg="white")
        title.place(x=0,y=0,width=1280,height=45)
        
        #Student Button
        Face_Reg = Image.open(r"C:\Users\ankit\Desktop\New folder\Face.jpg")
        Face_Reg = Face_Reg.resize((200,200), Image.ANTIALIAS)
        self.photoFace_Reg=ImageTk.PhotoImage(Face_Reg)

        bt = Button(BgImage,image=self.photoFace_Reg, command=self.student_details, cursor="hand2")
        bt.place(x=100,y=100,width=200,height=200)

        bt_1 = Button(BgImage, text= "Student Registration",command=self.student_details, cursor="hand2",font=("times new roman",15,"bold"),fg="blue")
        bt_1.place(x=100,y=300, width=200, height=40)

        #Faculty Button
        Faculty_Reg = Image.open(r"C:\Users\ankit\Desktop\New folder\Face.jpg")
        Faculty_Reg = Faculty_Reg.resize((200,200), Image.ANTIALIAS)
        self.photoFaculty_Reg=ImageTk.PhotoImage(Faculty_Reg)

        bt = Button(BgImage,image=self.photoFaculty_Reg, command=self.faculty_details, cursor="hand2")
        bt.place(x=500,y=100,width=200,height=200)

        bt_1 = Button(BgImage, text= "Faculty Registration",command=self.faculty_details, cursor="hand2",font=("times new roman",15,"bold"),fg="blue")
        bt_1.place(x=500,y=300, width=200, height=40)

        #Subject Button
        Subject_Reg = Image.open(r"C:\Users\ankit\Desktop\New folder\Face.jpg")
        Subject_Reg = Faculty_Reg.resize((200,200), Image.ANTIALIAS)
        self.photoSubject_Reg=ImageTk.PhotoImage(Subject_Reg)

        bt = Button(BgImage,image=self.photoSubject_Reg, command=self.subject_details, cursor="hand2")
        bt.place(x=900,y=100,width=200,height=200)

        bt_1 = Button(BgImage, text= "Subjects",command=self.subject_details, cursor="hand2",font=("times new roman",15,"bold"),fg="blue")
        bt_1.place(x=900,y=300, width=200, height=40)

        #Time Table
        TimeTb = Image.open(r"C:\Users\ankit\Desktop\New folder\face_scan.jpg")
        TimeTb = TimeTb.resize((200,200), Image.ANTIALIAS)
        self.photoTimeTb=ImageTk.PhotoImage(TimeTb)

        TimeTb_bt = Button(BgImage,image=self.photoTimeTb, command=self.time_table,cursor="hand2")
        TimeTb_bt.place(x=700,y=400,width=200,height=200)

        TimeTb_bt_1 = Button(BgImage, text= "Time Table", command=self.time_table,cursor="hand2",font=("times new roman",15,"bold"),fg="blue")
        TimeTb_bt_1.place(x=700,y=600, width=200, height=40)


        #Face Detection Button
        Face_Det = Image.open(r"C:\Users\ankit\Desktop\New folder\face_scan.jpg")
        Face_Det = Face_Det.resize((200,200), Image.ANTIALIAS)
        self.photoFace_Det=ImageTk.PhotoImage(Face_Det)

        bt = Button(BgImage,image=self.photoFace_Det, command=self.attendance_details,cursor="hand2")
        bt.place(x=350,y=400,width=200,height=200)

        bt_1 = Button(BgImage, text= "Attendance", command=self.attendance_details,cursor="hand2",font=("times new roman",15,"bold"),fg="blue")
        bt_1.place(x=350,y=600, width=200, height=40)


    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Registration(self.new_window)

    def attendance_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance_Registration(self.new_window) 

    def faculty_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Faculty_Registration(self.new_window)

    def subject_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Subject(self.new_window) 

    def time_table(self):
        self.new_window=Toplevel(self.root)
        self.app=Time_Schedule(self.new_window)        


if __name__ == "__main__":
    root=Tk()  
    obj=Attendance_System(root)
    root.mainloop()        