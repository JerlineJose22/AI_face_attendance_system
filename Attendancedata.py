import tkinter as tk
from tkinter import ttk,font as tkFont
from tkcalendar import Calendar
import sqlite3
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def showAttendance():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    
    def save_as_csv(data,selected_date):
        global filename,date
        date=selected_date
        filename=f'Attendance/data_{selected_date}.csv'
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Name', 'Time', 'Date'])
            csvwriter.writerows(data)

    def retrieve_data(selected_date):
        cursor.execute("SELECT * FROM attendance WHERE date = ?", (selected_date,))
        data = cursor.fetchall()
        return data

    def update_table(selected_date):
        data = retrieve_data(selected_date)
        tree.delete(*tree.get_children())  
        for record in data:
            tree.insert('', 'end', values=record)
    
    def mail():
        def send_email():
            try:
                receiver_email = entry_box.get() 
                subject = f"{date} Attendance"
                attachment_path =filename
                # Create a multipart message
                message = MIMEMultipart()
                message['From'] = 'Enter Your sender mail her' 
                message['To'] = receiver_email
                message['Subject'] = subject
            except:
                statuslabel.config(text=f"Save CSV and Send Mail", fg='red')



            # Attach CSV file
            with open(attachment_path, 'rb') as file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {attachment_path}')
            message.attach(part)

            # Connect to SMTP server and send email
            smtp_server = 'smtp.gmail.com'  # Update with your SMTP server address
            smtp_port = 587  # Update with your SMTP server port
            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login('Your sender mail', 'Gamil app password') # go to your google account search app password 
                server.sendmail('sender mail', receiver_email, message.as_string())
                status_label.config(text=f"Mail Sent Successfully", fg='green')
                root.destroy()
            except:
                statuslabel.config(text=f"Enter Correct Reciever Mail", fg='red')
                
            finally:
                server.quit()


        root = tk.Tk()
        root.title("Email Sender")
        root.geometry('400x200')
        font_title = tkFont.Font(family='Helvetica', size=10, weight='bold')
        tk.Label(root,text="Enter Reciever Mail",
                        font=font_title).pack()
        def on_entry_click(event):
            if entry_box.get() == "Enter Reciever Mail":
                entry_box.delete(0, tk.END)  # Clear the placeholder text
                entry_box.config(fg='black')  # Change text color to black

        def on_entry_leave(event):
            if entry_box.get() == "":
                entry_box.insert(0, "Enter Reciever Mail ")  # Insert placeholder text
                entry_box.config(fg='grey')  # Change text color to grey
        # Create an Entry widget with placeholder text
        entry_box = tk.Entry(root, width=40, fg='grey')
        entry_box.insert(0, "Enter Reciever Mail")  # Insert placeholder text
        entry_box.bind('<FocusIn>', on_entry_click)  # Bind click event to clear placeholder text
        entry_box.bind('<FocusOut>', on_entry_leave)  # Bind leave event to insert placeholder text
        entry_box.place(x=70,y=50)
        tk.Button(root, text="Send", command=send_email,bd=5,font=("times new roman", 15),bg="black",fg="green",width=7).place(x=150,y=90)
        statuslabel = tk.Label(root, text="", fg='black')
        statuslabel.place(x=130,y=150)
        root.mainloop()
        
    def calendar_date_selected():
        selected_date = cal.selection_get().strftime('%d-%m-%y')
        update_table(selected_date)
        return selected_date
    
    
    def save_csv_button_clicked():
        
        selected_date = cal.selection_get().strftime('%d-%m-%y')
        data = retrieve_data(selected_date)
        save_as_csv(data,selected_date)
        status_label.config(text=f"CSV Saved successfully", fg='green')
        
        
        
    root = tk.Tk()
    root.title("Attendance Register")

    cal = Calendar(root, selectmode='day', year=2024, month=3, day=1)
    cal.pack()

    cal.bind("<<CalendarSelected>>", lambda event: calendar_date_selected())

    tree = ttk.Treeview(root, columns=('Name', 'Time', 'Date'), show='headings')
    tree.heading('Name', text='Name')
    tree.heading('Time', text='Time')
    tree.heading('Date', text='Date')
    tree.pack()

    btn_save_csv = tk.Button(root, text="Save as CSV", command=save_csv_button_clicked,bd=3,font=("times new roman", 15),bg="white",fg="black")
    btn_save_csv.pack()
    btn_send_mail= tk.Button(root,text="Send as mail",command=mail,bd=3,font=("times new roman", 15),bg="white",fg="red")
    btn_send_mail.pack()
    status_label = tk.Label(root, text="", fg='black')
    status_label.pack(pady=5)

    root.mainloop()

    conn.close()
# showAttendance()
