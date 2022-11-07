from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from face_reg import Face_Registration

class Attendance_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("500x700+0+0")
        self.root.title("Attendance System")

        #Bg Image
        img=Image.open(r"C:\Users\ankit\Desktop\New folder\itersoa.jpg")
        img=img.resize((500,700),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        BgImage = Label(self.root, image=self.photoimg)
        BgImage.place(x=0,y=0,width=500,height=700)

        title = Label(BgImage, text="ATTENDANCE SOFTWARE", font=("Times new roman", 25,"bold"),bg="white")
        title.place(x=0,y=0,width=500,height=45)
        
        #Registration Button
        Face_Reg = Image.open(r"C:\Users\ankit\Desktop\New folder\Face.jpg")
        Face_Reg = Face_Reg.resize((200,200), Image.ANTIALIAS)
        self.photoFace_Reg=ImageTk.PhotoImage(Face_Reg)

        bt = Button(BgImage,image=self.photoFace_Reg, command=self.face_details, cursor="hand2")
        bt.place(x=150,y=100,width=200,height=200)

        bt_1 = Button(BgImage, text= "Face Registration",command=self.face_details, cursor="hand2",font=("times new roman",15,"bold"),fg="blue")
        bt_1.place(x=150,y=300, width=200, height=40)

        #Detection Button
        Face_Det = Image.open(r"C:\Users\ankit\Desktop\New folder\face_scan.jpg")
        Face_Det = Face_Det.resize((200,200), Image.ANTIALIAS)
        self.photoFace_Det=ImageTk.PhotoImage(Face_Det)

        bt = Button(BgImage,image=self.photoFace_Det, cursor="hand2")
        bt.place(x=150,y=400,width=200,height=200)

        bt_1 = Button(BgImage, text= "Attendance", cursor="hand2",font=("times new roman",15,"bold"),fg="blue")
        bt_1.place(x=150,y=600, width=200, height=40)


    def face_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Registration(self.new_window)



if __name__ == "__main__":
    root=Tk()  
    obj=Attendance_System(root)
    root.mainloop()        