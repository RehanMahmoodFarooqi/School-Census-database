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
def delete_data(game_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = "DELETE FROM Game WHERE Game_ID = %s"
        cursor.execute(query, (game_id,))
        connection.commit()
        messagebox.showinfo("Success", f"Record with Game ID {game_id} deleted successfully")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# Function to handle deletion button click
def delete_record():
    try:
        game_id = int(game_id_entry.get())
        delete_data(game_id)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid Game ID")

# Function to set up the GUI for deleting records
def gui_setup():
    root = Tk()
    root.title("Delete Game Record")

    delete_frame = Frame(root, padx=10, pady=10)
    delete_frame.pack(padx=50, pady=50)

    game_id_label = Label(delete_frame, text="Game ID to Delete:", font=("Helvetica", 16))
    game_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    global game_id_entry
    game_id_entry = Entry(delete_frame, font=("Helvetica", 16))
    game_id_entry.grid(row=0, column=1, padx=10, pady=10)

    delete_button = Button(delete_frame, text="Delete Record", command=delete_record, font=("Helvetica", 16))
    delete_button.grid(row=1, column=0, columnspan=2, pady=20)

    root.mainloop()


