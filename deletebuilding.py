import mysql.connector
from tkinter import *
from tkinter import messagebox

# Function to establish database connection
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='raniii12@',
        database='schoolsystem'
    )

# Function to handle deletion of data
def delete_data(building_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "DELETE FROM Building WHERE Building_ID = %s"
        cursor.execute(query, (building_id,))
        connection.commit()
        messagebox.showinfo("Success", f"Record with Building ID {building_id} deleted successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to handle deletion button click
def delete_record():
    try:
        building_id = int(building_id_entry.get())
        delete_data(building_id)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid Building ID")

# Function to set up the GUI for deleting records
def gui_setup():
    root = Tk()
    root.title("Delete Building Record")

    delete_frame = Frame(root, padx=10, pady=10)
    delete_frame.pack(padx=50, pady=50)

    building_id_label = Label(delete_frame, text="Building ID to Delete:", font=("Helvetica", 16))
    building_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global building_id_entry
    building_id_entry = Entry(delete_frame, font=("Helvetica", 16))
    building_id_entry.grid(row=0, column=1, padx=10, pady=10)

    delete_button = Button(delete_frame, text="Delete Record", command=delete_record, font=("Helvetica", 16))
    delete_button.grid(row=1, column=0, columnspan=2, pady=20)

    root.mainloop()


