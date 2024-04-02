import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import PIL
import Add_new_face
import Attendance_taker
import Attendancedata
import remove_student

#Main GUI Frame
window = Tk()
window.title("AI Face Attendance")
window.geometry("1300x720")
window.configure(background="white")


PIL.Image.ANTIALIAS = PIL.Image.LANCZOS
titl = tk.Label(window, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
titl.pack(fill=X)

titl = tk.Label(
    window, text="Park College of Engineering and Technology", bg="black", fg="yellow", font=("arial", 27),
)
titl.place(x=300, y=12)

a = tk.Label(
    window,
    text="AI Face Attendance System",
    bg="white",
    fg="black",
    bd=10,
    font=("arial", 35),
)
a.pack()

#Gui Images
ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("UI_Image/attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=1010, y=270)

vi = Image.open("UI_Image/verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=550, y=270)

#Buttons

def TakeImageUI():
    Add_new_face.main() # Call Main Fuction from Add_new_face.py
    
    
r = tk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=100, y=520)


def automatic_attedance():
    Attendance_taker.main() # Call Main Fuction from Attendance_taker.py


r = tk.Button(
    window,
    text="Make Attendance",
    command=automatic_attedance,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=550, y=520)


def view_attendance():
    Attendancedata.showAttendance() # Call ShowAttendance fuction from attendancedata.py


r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=1000, y=520)

def Remove_student():
    remove_student.main() # Call Main Fuction from remove_student.py
    

r=tk.Button(text='Remove Student',command= Remove_student,bd=5,font=("times new roman", 16),
    bg="red",
    fg="black",
    height=1,
    width=15,).place(x=570,y=650)

window.mainloop()