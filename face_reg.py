from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Registration:
    def __init__(self, root):
        self.root=root
        self.root.geometry("500x700+0+0")
        self.root.title("Attendance System")

        #variables
        self.var_Name=StringVar()
        self.var_Roll=StringVar()
        self.var_branch=StringVar()
        self.var_Sem=StringVar()


        #Bg Image
        bg_img=Image.open(r"C:\Users\ankit\Desktop\New folder\itersoa.jpg")
        bg_img=bg_img.resize((500,700),Image.ANTIALIAS)
        self.photobg_img=ImageTk.PhotoImage(bg_img)

        BgImage = Label(self.root, image=self.photobg_img)
        BgImage.place(x=0,y=0,width=500,height=700)

        title = Label(BgImage, text="Facial Registration", font=("Times new roman", 25,"bold"),bg="white")
        title.place(x=0,y=0,width=500,height=45)

        main_frame = Frame(BgImage, bd=2, bg="white")
        main_frame.place(x=20,y=50,width=450, height = 650)

        #Details Frame
        det_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"), bg="white")
        det_frame.place(x=10, y=10, width=400, height=300)

        #Name
        Name_label=Label(det_frame,text="Name:", font=("times new roman", 12,"bold"),bg="white")
        Name_label.grid(row=0, column=0, padx=10, sticky=W)

        Name_Entry=Entry(det_frame, textvariable=self.var_Name,width=23,font=("times new roman",12,"bold"),bg="white")
        Name_Entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #Roll No
        Roll_label=Label(det_frame,text="Roll No:", font=("times new roman", 12,"bold"),bg="white")
        Roll_label.grid(row=1, column=0, padx=10, sticky=W)

        Roll_Entry=Entry(det_frame, textvariable=self.var_Roll,width=23,font=("times new roman",12,"bold"),bg="white")
        Roll_Entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #Branch
        dep_label=Label(det_frame,text="Branch", font=("times new roman", 12,"bold"),bg="white")
        dep_label.grid(row=2,column=0, padx=10)

        dep_combo=ttk.Combobox(det_frame, textvariable=self.var_branch,font=("times new roman",12,"bold"), state="readonly")
        dep_combo["values"]=("Select Branch", "CSE", "CSIT", "EEE", "ECE", "MECH", "Civil")
        dep_combo.current(0)
        dep_combo.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        #Semester
        dep_label=Label(det_frame,text="Semester", font=("times new roman", 12,"bold"),bg="white")
        dep_label.grid(row=3,column=0, padx=10)

        dep_combo=ttk.Combobox(det_frame, textvariable=self.var_Sem, font=("times new roman",12,"bold"), state="readonly")
        dep_combo["values"]=("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th","7th", "8th")
        dep_combo.current(0)
        dep_combo.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        #radiobuttons
        self.var_radio1=StringVar()
        radiobt_1=ttk.Radiobutton(det_frame, variable=self.var_radio1, text="Take photo Sample", value="Yes")
        radiobt_1.grid(row=4,column=0)

        radiobt_1=ttk.Radiobutton(det_frame, variable=self.var_radio1,text="No photo Sample", value="No")
        radiobt_1.grid(row=4,column=1)

        #Buttons
        Bt_frame=Frame(main_frame,bd=2,relief=RIDGE,bg="white")
        Bt_frame.place(x=10, y=240, width=400,height=35)
        
        save_photo_bt=Button(Bt_frame,text="Save", command=self.add_data ,width=10,font=("times new roman", 12,"bold"),bg="white")
        save_photo_bt.grid(row=0,column=0)

        delete_bt=Button(Bt_frame,text="DELETE", command=self.delete_data,width=10,font=("times new roman", 12,"bold"),bg="white")
        delete_bt.grid(row=0,column=1)

        reset_bt=Button(Bt_frame,text="Reset", command=self.reset_data, width=10,font=("times new roman", 12,"bold"),bg="white")
        reset_bt.grid(row=0,column=2)

        Update_bt=Button(Bt_frame,text="Update",command=self.update_data, width=10,font=("times new roman", 12,"bold"),bg="white")
        Update_bt.grid(row=0,column=3)

        Bt_frame1=Frame(main_frame,bd=2,relief=RIDGE,bg="white")
        Bt_frame1.place(x=10, y=275, width=400,height=35)

        take_photo_bt=Button(Bt_frame1,text="Take Photo", command=self.data_generate, width=21,font=("times new roman", 12,"bold"),bg="white")
        take_photo_bt.grid(row=0,column=0)
                
        train_photo_bt=Button(Bt_frame1,text="Train Photo", command=self.train_classifier,width=21,font=("times new roman", 12,"bold"),bg="white")
        train_photo_bt.grid(row=0,column=1)



        #Details Fetch Frame
        Search_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text="Search System", font=("times new roman",12,"bold"), bg="white")
        Search_frame.place(x=10, y=320, width=400, height=70)

        #Search
        search_label=Label(Search_frame,text="Search by:", font=("times new roman", 12,"bold"),bg="blue")
        search_label.grid(row=0, column=0, padx=2, sticky=W)

        search_combo=ttk.Combobox(Search_frame, font=("times new roman",12,"bold"), state="readonly", width=7)
        search_combo["values"]=("Select", "Roll No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        roll_Entry=Entry(Search_frame, width=11,font=("times new roman",12,"bold"),bg="white")
        roll_Entry.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        search_bt=Button(Search_frame,text="Search", width=6,font=("times new roman", 11,"bold"),bg="white")
        search_bt.grid(row=0,column=3, padx=2)
                
        showall_bt=Button(Search_frame,text="Show all", width=6,font=("times new roman", 11,"bold"),bg="white")
        showall_bt.grid(row=0,column=4, padx=2)

        #Student details frame
        table_frame=Frame(main_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=400, width=400, height=230)

        
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, column=("name", "rollno", "branch", "semester", "photo"), yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("name", text="Name")
        self.student_table.heading("rollno", text="Roll_No")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("branch", text="Branch")
        self.student_table.heading("photo", text="Photo Sample")

        self.student_table["show"]="headings"

        self.student_table.column("name", width=70)
        self.student_table.column("rollno", width=50)
        self.student_table.column("semester", width=35)
        self.student_table.column("branch", width=35)
        self.student_table.column("photo", width=40)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    
    #Add Data
    def add_data(self):
        if self.var_branch.get()=="Select branch" or self.var_Name.get()=="" or self.var_Roll.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                my_cursor = conn.cursor()  
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s)", (
                                                            self.var_Name.get(),
                                                            self.var_Roll.get(),
                                                            self.var_Sem.get(),
                                                            self.var_branch.get(),
                                                            self.var_radio1.get()
                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Details added successfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}")   

    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
        my_cursor = conn.cursor()  
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END, values=i)                                      
            conn.commit()
        conn.close() 


    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus() 
        content=self.student_table.item(cursor_focus)   
        data=content["values"]

        self.var_Name.set(data[0]),
        self.var_Roll.set(data[1]),
        self.var_Sem.set(data[2]),
        self.var_branch.set(data[3]),
        self.var_radio1.set(data[4])

    #update
    def update_data(self):
        if self.var_branch.get()=="Select branch" or self.var_Name.get()=="" or self.var_Roll.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                Update=messagebox.askyesno("Update", "Do you want to update the details?")  
                if Update>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                    my_cursor = conn.cursor() 
                    my_cursor.execute("Update student set Name=%s, Semester=%s, Branch=%s, PhotoSample=%s where Roll_No=%s", (
                                                                                                                    self.var_Name.get(),
                                                                                                                    self.var_Sem.get(),
                                                                                                                    self.var_branch.get(),
                                                                                                                    self.var_radio1.get(),
                                                                                                                    self.var_Roll.get()
                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details added successfully", parent=self.root)        
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}")

    #delete
    def delete_data(self):
        if self.var_Roll.get()=="":
            messagebox.showerror("Error", "Roll No is mandatory")
        else:
            try:
                delete=messagebox.askyesno("Delete", "Do you want to delete the details?")   
                if delete>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                    my_cursor = conn.cursor() 
                    sql="delete from student where Roll_No=%s"
                    val=(self.var_Roll.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student details deleted successfully", parent=self.root)  
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}")    

    #reset
    def reset_data(self):
        self.var_Name.set("")
        self.var_Roll.set("")
        self.var_Sem.set("Select Semester")
        self.var_branch.set("Select Branch")
        self.var_radio1.set("")

    #Photo Sample
    def data_generate(self):
        id = (self.var_Roll.get())
        
        if self.var_branch.get()=="Select branch" or self.var_Name.get()=="" or self.var_Roll.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                my_cursor = conn.cursor() 
                my_cursor.execute("select * from student")
                result=my_cursor.fetchall()  

                

                sql="""update student set Name=%s, Semester=%s, Branch=%s, PhotoSample=%s where Roll_No=%s"""
                
                val= (
                        self.var_Name.get(),
                        self.var_Sem.get(),
                        self.var_branch.get(),
                        self.var_radio1.get(),

                        self.var_Roll.get()
                    )
                my_cursor.execute(sql, val)  
            
                conn.commit()
                self.fetch_data()
                self.reset_data()  
                conn.close()

                def is_number(s):
                    try:
                        float(s)
                        return True
                    except ValueError:
                        pass
                
                    try:
                        import unicodedata
                        unicodedata.numeric(s)
                        return True
                    except (TypeError, ValueError):
                        pass
                
                    return False

                if(is_number(id)):
                    cam = cv2.VideoCapture(0)
                    harcascadePath = "haarcascade_frontalface_default.xml"
                    face_classifier = detector = cv2.CascadeClassifier(harcascadePath)
                    sampleNum = 0
                    
                    while(True):
                        ret, img = cam.read()
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)
                        for(x,y,w,h) in faces:
                            cv2.rectangle(img, (x, y), (x+w, y+h), (10, 159, 255), 2)
                            sampleNum = sampleNum+1
                            #saving the captured face in the dataset folder TrainingImage
                            cv2.imwrite("data/image." + id + '.' +str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                            cv2.imshow('frame', img)
                        if cv2.waitKey(30) & 0xFF == ord('q'):
                            break
                        elif sampleNum > 30:
                            break
                    cam.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data set successfully")
                        

            except Exception as es:
                print(es)
                #messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)



    #train data
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[-1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")

if __name__ == "__main__":
    root=Tk()  
    obj=Face_Registration(root)
    root.mainloop()        