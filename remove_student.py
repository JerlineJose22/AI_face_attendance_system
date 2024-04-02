import csv
import tkinter as tk
from tkinter import *
import shutil

def main():
    def remove_student():
    # Define the CSV file path
        input_name_char = input_name.get()
        input_rollno_char= input_rollno.get()
        
        csv_file = "data/features_all.csv"

        # Define the value to match in the first column
        value_to_match = input_name_char+"_"+input_rollno_char
        value_to_match=value_to_match.upper()
        # Initialize a variable to store the found row (if any)
        found_row = None

        # Read the CSV file and search for the specific value in the first column
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == value_to_match:  # Check if the first column value matches the specified value
                    found_row = row
                    break  # Stop searching once the row is found

        combined_columns=''
        if found_row:
            combined_columns = '_'.join(found_row[:3])  # Combine the first two columns with underscores
            folder_path ="data/data_faces_from_camera/"+ combined_columns
            try:
                shutil.rmtree(folder_path)  # Remove the folder and its contents
                status_label.config(text=f"Student removed successfully.", fg='green')
            except OSError as e:
                status_label.config(text=f"Error: {e}", fg='red')
        else:
            status_label.config(text=f"Student is not found.", fg='red')
    #Remove from CSV 
        rows = []
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                
                rows.append(row)

        # Filter out rows where the first column matches the specified value
        filtered_rows = [row for row in rows if row[2] != value_to_match]

        # Write the filtered data back to the CSV file
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(filtered_rows)

    # Remove CSV and All data
    def GUI_clear_data():
        #  "/data_faces_from_camera/person_x/"...
        csv_file="data/features_all.csv"
        folder_path ="data/data_faces_from_camera/"
        try:
            shutil.rmtree(folder_path)
            with open(csv_file, mode='w', newline='') as file:
                file.write('')
            status_label.config(text=f"Face images and `features_all.csv` removed!", fg='red')
        except OSError as e:
            status_label.config(text=f"No Data Found", fg='red')
        with open(csv_file, mode='w', newline='') as file:
            file.write('')
        status_label.config(text=f"Face images and `features_all.csv` removed!{e}", fg='red')

        

    window = tk.Toplevel()
    window.title("Remove Student")
    window.geometry('800x350')

    input_name = tk.Entry(window, width=70,bd=3)
    
            
    input_rollno= tk.Entry(window, width=70,bd=3)

    tk.Label(window,text="Remove Student",font=("arial", 20)).pack()
    tk.Label(window,text="Name : ",font=("arial",13)).place(x=150,y=100)
    input_name.place(x=260,y=100)
    tk.Label(window,text="Roll Number :",font=("arial",12)).place(x=150,y=150)
    input_rollno.place(x=260,y=150)
    status_label = tk.Label(window, text="", fg='black')
    status_label.pack(pady=5)

    tk.Button(window,text='Remove',command=remove_student,bd=5,font=("times new roman", 16),
        bg="black",
        fg="yellow",
        height=1,
        width=7,).place(x=350,y=230)
    tk.Button(window,text='Remove All Data',command=GUI_clear_data,bd=5,font=("times new roman", 16),
        bg="red",
        fg="black",
        height=1,
        width=15,).place(x=300,y=290)

    window.mainloop()
