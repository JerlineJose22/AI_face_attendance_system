import tkinter as tk
from tkinter import *
import lecture1
import lecture2
import lecture3
import lecture4
import lecture5

def Select_lecture():
    window = Tk()
    window.title("Select Lecture")
    window.geometry("400x600")
    window.configure(background="white")

    a = tk.Label(
        window,
        text="Select Lecture",
        bg="white",
        fg="black",
        bd=5,
        font=("arial", 20),
    )
    a.pack()

    def lecture_1():
        lecture1.main()
        
    r = tk.Button(
        window,
        text="Lecture 1",
        command=lecture_1,
        bd=10,
        font=("times new roman", 13),
        bg="yellow",
        fg="black",
        height=1,
        width=15,
    )
    r.place(x=100, y=100)
    
    def lecture_2():
        lecture2.main()
        
    r = tk.Button(
        window,
        text="Lecture 2",
        command=lecture_2,
        bd=10,
        font=("times new roman", 13),
        bg="yellow",
        fg="black",
        height=1,
        width=15,
    )
    r.place(x=100, y=200)
    
    def lecture_3():
        lecture3.main()
        
    r = tk.Button(
        window,
        text="Lecture 3",
        command=lecture_3,
        bd=10,
        font=("times new roman", 13),
        bg="yellow",
        fg="black",
        height=1,
        width=15,
    )
    r.place(x=100, y=300)
    
    def lecture_4():
        lecture4.main()
        
    r = tk.Button(
        window,
        text="Lecture 4",
        command=lecture_4,
        bd=10,
        font=("times new roman", 13),
        bg="yellow",
        fg="black",
        height=1,
        width=15,
    )
    r.place(x=100, y=400)
    
    def lecture_5():
        lecture5.main()
        
    r = tk.Button(
        window,
        text="Lecture 5",
        command=lecture_5,
        bd=10,
        font=("times new roman", 13),
        bg="yellow",
        fg="black",
        height=1,
        width=15,
    )
    r.place(x=100, y=500)
    
    
    window.mainloop()