from tkinter import *
from tkinter import ttk
  
root=Tk()
 
# setting the windows size
root.geometry("300x200")
  
# declaring string variable
# for storing name and password
name_var=StringVar()
 
  
# defining a function that will
# get the name and password and
# print them on the screen
def submit():
 
    name=name_var.get()
    print("The name is : " + name)
    #name_var.set("")
    
    
     
     
# creating a label for
# name using widget Label
name_label = Label(root, text = 'Username', font=('calibre',10, 'bold'))
  
# creating a entry for input
# name using widget Entry
name_entry = Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
  
# creating a button using the widget
# Button that will call the submit function
sub_btn=Button(root,text = 'Submit', command = submit)
  
# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=1,column=0)
name_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
  
# performing an infinite loop
# for the window to display
root.mainloop()

str(submit)