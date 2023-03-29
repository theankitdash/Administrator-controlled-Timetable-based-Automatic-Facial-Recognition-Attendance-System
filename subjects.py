from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Subject:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1140x370+0+0")
        self.root.title("Subject Details")

        self.var_sub=StringVar()
        self.var_subCode=StringVar()

        title = Label(self.root, text="SUBJECT DETAILS", font=("Times new roman", 25,"bold"),bg="white")
        title.place(x=0,y=0,width=1280,height=45)

        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=0,y=50,width=1240, height = 400)

        #Details Frame
        det_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text="Subject Details", font=("times new roman",14,"bold"), bg="white")
        det_frame.place(x=5, y=10, width=400, height=220)

        #SubCode
        SubCode_label=Label(det_frame,text="Subject Code:", font=("times new roman", 14,"bold"),bg="white")
        SubCode_label.grid(row=0,column=0, padx=10,  pady=15)

        SubCode_Entry=Entry(det_frame, textvariable=self.var_subCode,width=23,font=("times new roman",14,"bold"),bg="white")
        SubCode_Entry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #Subject
        Subject_label=Label(det_frame,text="Subject:", font=("times new roman", 14,"bold"),bg="white")
        Subject_label.grid(row=1,column=0, padx=10, pady=10)

        Subject_Entry=Entry(det_frame, textvariable=self.var_sub,width=23,font=("times new roman",14,"bold"),bg="white")
        Subject_Entry.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #radiobuttons
        self.var_radio1=StringVar()
        radiobt_1=ttk.Radiobutton(det_frame, variable=self.var_radio1, text="Theory", value="Theory")
        radiobt_1.grid(row=2,column=0, padx=15, pady=10)

        radiobt_1=ttk.Radiobutton(det_frame, variable=self.var_radio1,text="Practical", value="Practical")
        radiobt_1.grid(row=2,column=1, padx=2, pady=10)

        #Buttons
        Bt_frame=Frame(main_frame,bd=2,relief=RIDGE,bg="white")
        Bt_frame.place(x=5, y=250, width=404,height=35)
        
        save_photo_bt=Button(Bt_frame,text="Save", command=self.add_data ,width=10,font=("times new roman", 12,"bold"),bg="white")
        save_photo_bt.grid(row=0,column=0)

        delete_bt=Button(Bt_frame,text="DELETE", command=self.delete_data,width=10,font=("times new roman", 12,"bold"),bg="white")
        delete_bt.grid(row=0,column=1)

        reset_bt=Button(Bt_frame,text="Reset", command=self.reset_data, width=10,font=("times new roman", 12,"bold"),bg="white")
        reset_bt.grid(row=0,column=2)

        Update_bt=Button(Bt_frame,text="Update",command=self.update_data, width=10,font=("times new roman", 12,"bold"),bg="white")
        Update_bt.grid(row=0,column=3)

        #Details Fetch Frame
        Search_frame=LabelFrame(main_frame, bd=2, relief=RIDGE, text="Search System", font=("times new roman",14,"bold"), bg="white")
        Search_frame.place(x=420, y=10, width=700, height=80)

        #Search
        search_label=Label(Search_frame,text="Search by:", font=("times new roman", 14,"bold"), width=10,bg="white")
        search_label.grid(row=0, column=0, padx=2, sticky=W)

        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(Search_frame, textvariable= self.var_com_search, font=("times new roman",14,"bold"), state="readonly", width=10)
        search_combo["values"]=("Select", "subcode")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        self.var_search=StringVar()
        roll_Entry=Entry(Search_frame,textvariable= self.var_search,width=15,font=("times new roman",14,"bold"),bg="white")
        roll_Entry.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        search_bt=Button(Search_frame,command=self.search_data,text="Search", width=8,font=("times new roman", 14,"bold"),bg="white")
        search_bt.grid(row=0,column=3, padx=5)
                
        showall_bt=Button(Search_frame,command=self.fetch_data,text="Show all", width=10,font=("times new roman", 14,"bold"),bg="white")
        showall_bt.grid(row=0,column=4, padx=5)

        #Subject details frame
        table_frame=Frame(main_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=420, y=100, width=700, height=200)

        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.subject_table=ttk.Treeview(table_frame, column=("subcode", "subject", "SubType"), yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.subject_table.yview)

        self.subject_table.heading("subcode", text="Subject Code")
        self.subject_table.heading("subject", text="Subject")
        self.subject_table.heading("SubType", text="Subject Type")


        self.subject_table["show"]="headings"

        self.subject_table.column("subcode", width=10)
        self.subject_table.column("subject", width=200)
        self.subject_table.column("SubType", width=10)
        

        self.subject_table.pack(fill=BOTH, expand=1)
        self.subject_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #Add Data
    def add_data(self):
        if self.var_sub.get()=="" or self.var_subCode.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                my_cursor = conn.cursor()  
                my_cursor.execute("insert into subjects values(%s,%s,%s)", (
                                                            self.var_subCode.get(),
                                                            self.var_sub.get(),
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
        my_cursor.execute("Select * from subjects")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.subject_table.delete(*self.subject_table.get_children())
            for i in data:
                self.subject_table.insert("",END, values=i)                                      
            conn.commit()
        conn.close() 


    def get_cursor(self, event=""):
        cursor_focus=self.subject_table.focus() 
        content=self.subject_table.item(cursor_focus)   
        data=content["values"]

        self.var_subCode.set(data[0]),
        self.var_sub.set(data[1]),
        self.var_radio1.set(data[2])
        
    #update
    def update_data(self):
        if self.var_sub.get()=="" or self.var_subCode.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                Update=messagebox.askyesno("Update", "Do you want to update the details?")  
                if Update>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                    my_cursor = conn.cursor() 
                    my_cursor.execute("Update subjects set SUBNAME=%s, SUBTYPE=%s where SUBCODE=%s", (
                                                                                                                    
                                                                                                                    self.var_sub.get(),
                                                                                                                    self.var_radio1.get(),
                                                                                                                    self.var_subCode.get()
                                                                                                                    
                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Subject details added successfully", parent=self.root)        
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}")

    #delete
    def delete_data(self):
        if self.var_sub.get()=="" or self.var_subCode.get()=="":
            messagebox.showerror("Error", "Subject is mandatory")
        else:
            try:
                delete=messagebox.askyesno("Delete", "Do you want to delete the details?")   
                if delete>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                    my_cursor = conn.cursor() 
                    sql="delete from subjects where SUBCODE=%s"
                    val=(self.var_subCode.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Subject details deleted successfully", parent=self.root)  
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}")    

    #reset
    def reset_data(self):
        self.var_subCode.set("")
        self.var_sub.set("")
        self.var_radio1.set("")

    #search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select option")   
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Chiku@3037', database='attendance-system')
                my_cursor = conn.cursor() 
                my_cursor.execute("select * from subjects where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows=my_cursor.fetchall()

                if len(rows)!=0:
                    self.subject_table.delete(*self.subject_table.get_children())
                    for i in rows:
                        self.subject_table.insert("",END,values=i)


                    conn.commit()
                conn.close()        
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}")



if __name__ == "__main__":
    root=Tk()  
    obj=Subject(root)
    root.mainloop()           