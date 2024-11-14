import tkinter as tk
from tkinter import messagebox, font as tkfont
import insertbuilding as IB
import insertschooll as IS
import insertbuildinglab as IBL
import insertcontact_info as ICI
import insertgame as IG
import insertgameschool as IGS
import inserthead as IH
import insertlab as IL 
import insertuc as IUC

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple CRUD Application")
        self.geometry("600x400")  # Adjust initial window size as needed
        
        self.create_widgets()
        
    def create_widgets(self):
        # Configure row and column weights for resizing
        for i in range(7):  # Adjusting for new row and rows after
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Default font size
        self.font_size = 20  # Fixed font size for stability
        self.custom_font = tkfont.Font(size=self.font_size)
        
        # Welcome Message
        self.welcome_label = tk.Label(self, text="Welcome to School System Database", font=("Helvetica", 24))
        self.welcome_label.grid(row=0, column=0, sticky="nsew")
        
        # Insert Button
        self.insert_button = tk.Button(self, text="Insert", command=lambda: self.show_menu("Insert"), font=self.custom_font, bg="grey")
        self.insert_button.grid(row=1, column=0, sticky="nsew")
        
        # Delete Button
        self.delete_button = tk.Button(self, text="Delete", command=lambda: self.show_menu("Delete"), font=self.custom_font, bg="grey")
        self.delete_button.grid(row=2, column=0, sticky="nsew")
        
        # Modify Button
        self.modify_button = tk.Button(self, text="Modify", command=lambda: self.show_menu("Modify"), font=self.custom_font, bg="grey")
        self.modify_button.grid(row=3, column=0, sticky="nsew")
        
        # Search Button
        self.search_button = tk.Button(self, text="Search", command=lambda: self.show_menu("Search"), font=self.custom_font, bg="grey")
        self.search_button.grid(row=4, column=0, sticky="nsew")
        
        # Display Button (new button)
        self.display_button = tk.Button(self, text="Display", command=lambda: self.show_menu("Display"), font=self.custom_font, bg="grey", fg="black")
        self.display_button.grid(row=5, column=0, sticky="nsew")
        
    def show_menu(self, action):
        menu_window = tk.Toplevel(self)
        menu_window.title(f"{action} Menu")
        menu_window.geometry("300x250")
        
        options = [
            "Building", "Building_Lab", "Contact_Info", "Game",
            "Game_School", "Head", "Lab", "School", "Union_Council"
        ]
        
        for option in options:
            button = tk.Button(menu_window, text=option, command=lambda opt=option: self.menu_action(opt, action), bg="grey")
            button.pack(fill=tk.BOTH, expand=True)
        
    def menu_action(self, option, action):
        if action == "Insert":
            if option == "Building":
                self.insert_building()
            elif option == "Building_Lab":
                self.insert_building_lab()
            elif option == "Contact_Info":
                self.insert_contact_info()
            elif option == "Game":
                self.insert_game()
            elif option == "Game_School":
                self.insert_game_school()
            elif option == "Head":
                self.insert_head()
            elif option == "Lab":
                self.insert_lab()
            elif option == "School":
                self.insert_school()
            elif option == "Union_Council":
                self.insert_union_council()
        elif action == "Delete":
            pass  # Implement delete action logic here
        elif action == "Modify":
            pass  # Implement modify action logic here
        elif action == "Search":
            pass  # Implement search action logic here
        elif action == "Display":
            pass  # Implement display action logic here

    def insert_building(self):
        IB.gui_setup()

    def insert_building_lab(self):
        IBL.gui_setup()

    def insert_contact_info(self):
        ICI.gui_setup()

    def insert_game(self):
        IG.gui_setup()

    def insert_game_school(self):
        IGS.gui_setup()

    def insert_head(self):
        IH.gui_setup()

    def insert_lab(self):
        IL.gui_setup()

    def insert_school(self):
        IS.gui_setup()

    def insert_union_council(self):
        IUC.gui_setup()

    def on_resize(self, event):
        # Adjust font size based on window size
        new_size = min(event.width // 15, event.height // 8)
        self.custom_font.configure(size=new_size)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
