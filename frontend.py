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
import deleteschool as DS 
import deletebuilding as DB 
import deletecontactinfo as DCI 
import deletegame as DG 
import deletehead as DH 
import deletelab as DL 
import deleteuc as DC 
import deletebuildinglab as DBL 
import deleteschoolgame as DSG 
import searchschool as SS 
import searchuc as SUC 
import searchlab as SL
import searchhead as SH 
import searchgame as SG 
import searchcontactinfo as SCI 
import searchbuilding as SB
import searchgameschool as SGS 
import searchbuildinglab as SBL 
import displayschool as DIS 
import displaybuilding as DIB 
import displaybuildinglab as DIBL 
import displaycontactinfo as DICI 
import displaygame as DIG 
import displaygameschool as DIGS 
import displayhead as DIH 
import displaylab as DIL 
import displayuc as DIUC 
import modifyschool as MS 
import modifybuilding as MB 
import modifycontactinfo as MCI 
import modifygame as MG 
import modifyhead as MH 
import modifylab as ML 
import modifyuc as MUC 


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("School System Database")
        self.geometry("600x400")  # Adjust initial window size as needed
        self.configure(bg='#f0f0f0')  # Set background color
        self.create_widgets()
        self.add_background_image()
        
    def create_widgets(self):
        # Configure row and column weights for resizing
        for i in range(7):  # Adjusting for new row and rows after
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Default font size
        self.font_family = "Arial"
        self.font_size = 18  # Adjusted font size
        self.custom_font = tkfont.Font(family=self.font_family, size=self.font_size)
        
        # Welcome Message
        self.welcome_label = tk.Label(self, text="Welcome to School System Database", font=(self.font_family, 24), bg='#4CAF50', fg='white', pady=10)
        self.welcome_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)
        
        # Insert Button
        self.insert_button = tk.Button(self, text="Insert", command=lambda: self.show_menu("Insert"), font=self.custom_font, bg="#2196F3", fg="white", pady=10)
        self.insert_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        
        # Delete Button
        self.delete_button = tk.Button(self, text="Delete", command=lambda: self.show_menu("Delete"), font=self.custom_font, bg="#f44336", fg="white", pady=10)
        self.delete_button.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        
        # Modify Button
        self.modify_button = tk.Button(self, text="Modify", command=lambda: self.show_menu("Modify"), font=self.custom_font, bg="#FF9800", fg="white", pady=10)
        self.modify_button.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)
        
        # Search Button
        self.search_button = tk.Button(self, text="Search", command=lambda: self.show_menu("Search"), font=self.custom_font, bg="#9C27B0", fg="white", pady=10)
        self.search_button.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)
        
        # Display Button (new button)
        self.display_button = tk.Button(self, text="Display", command=lambda: self.show_menu("Display"), font=self.custom_font, bg="#00BCD4", fg="white", pady=10)
        self.display_button.grid(row=5, column=0, sticky="nsew", padx=10, pady=5)
        
    def add_background_image(self):
        # Add a label with a background image
        image_path = "computer_image.png"  # Replace with your image file path
        try:
            background_image = tk.PhotoImage(file=image_path)
            background_label = tk.Label(self, image=background_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            background_label.image = background_image  # Keep a reference
        except tk.TclError:
            print(f"Failed to load image from {image_path}")
        
    def show_menu(self, action):
        menu_window = tk.Toplevel(self)
        menu_window.title(f"{action} Menu")
        menu_window.geometry("300x250")
        menu_window.configure(bg='#f0f0f0')  # Set background color
        
        options = [
            "Building", "Building_Lab", "Contact_Info", "Game",
            "Game_School", "Head", "Lab", "School", "Union_Council"
        ]
        
        for option in options:
            button = tk.Button(menu_window, text=option, command=lambda opt=option: self.menu_action(opt, action), bg="#607D8B", fg="white", pady=5)
            button.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
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
            if option == "Building":
                self.delete_building()
            elif option == "Building_Lab":
                self.delete_building_lab()
            elif option == "Contact_Info":
                self.delete_contact_info()
            elif option == "Game":
                self.delete_game()
            elif option == "Game_School":
                self.delete_game_school()
            elif option == "Head":
                self.delete_head()
            elif option == "Lab":
                self.delete_lab()
            elif option == "School":
                self.delete_school()
            elif option == "Union_Council":
                self.delete_union_council()
        elif action == "Modify":
            if option == "Building":
                self.modify_building()
            elif option == "Building_Lab":
                messagebox.showerror("Modification Error", "This table could not be modified.")
            elif option == "Contact_Info":
                self.modify_contact_info()
            elif option == "Game":
                self.modify_game()
            elif option == "Game_School":
                messagebox.showerror("Modification Error", "This table could not be modified.")
            elif option == "Head":
                self.modify_head()
            elif option == "Lab":
                self.modify_lab()
            elif option == "School":
                self.modify_school()
            elif option == "Union_Council":
                self.modify_union_council()
        elif action == "Search":
            if option == "Building":
                self.search_building()
            elif option == "Building_Lab":
                self.search_building_lab()
            elif option == "Contact_Info":
                self.search_contact_info()
            elif option == "Game":
                self.search_game()
            elif option == "Game_School":
                self.search_game_school()
            elif option == "Head":
                self.search_head()
            elif option == "Lab":
                self.search_lab()
            elif option == "School":
                self.search_school()
            elif option == "Union_Council":
                self.search_union_council()
        elif action == "Display":
            if option == "Building":
                self.display_building()
            elif option == "Building_Lab":
                self.display_building_lab()
            elif option == "Contact_Info":
                self.display_contact_info()
            elif option == "Game":
                self.display_game()
            elif option == "Game_School":
                self.display_game_school()
            elif option == "Head":
                self.display_head()
            elif option == "Lab":
                self.display_lab()
            elif option == "School":
                self.display_school()
            elif option == "Union_Council":
                self.display_union_council()

    # Function for insertion
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

    # Function for deletion
    def delete_building(self):
        DB.gui_setup()
    def delete_building_lab(self):
        DBL.gui_setup()
    def delete_contact_info(self):
        DCI.gui_setup()
    def delete_game(self):
        DG.gui_setup()
    def delete_game_school(self):
        DSG.gui_setup()
    def delete_head(self):
        DH.gui_setup()
    def delete_lab(self):
        DL.gui_setup()
    def delete_school(self):
        DS.gui_setup()
    def delete_union_council(self):
        DC.gui_setup()

    # Function for modification
    def modify_building(self):
        MB.gui_setup()
    def modify_contact_info(self):
        MCI.gui_setup()
    def modify_game(self):
        MG.gui_setup()
    def modify_head(self):
        MH.gui_setup()
    def modify_lab(self):
        ML.gui_setup()
    def modify_school(self):
        MS.gui_setup()
    def modify_union_council(self):
        MUC.gui_setup()

    # Function for search
    def search_building(self):
        SB.gui_setup()
    def search_building_lab(self):
        SBL.gui_setup()
    def search_contact_info(self):
        SCI.gui_setup()
    def search_game(self):
        SG.gui_setup()
    def search_game_school(self):
        SGS.gui_setup()
    def search_head(self):
        SH.gui_setup()
    def search_lab(self):
        SL.gui_setup()
    def search_school(self):
        SS.gui_setup()
    def search_union_council(self):
        SUC.gui_setup()

    # Function for display
    def display_building(self):
        DIB.gui_setup()
    def display_building_lab(self):
        DIBL.gui_setup()
    def display_contact_info(self):
        DICI.gui_setup()
    def display_game(self):
        DIG.gui_setup()
    def display_game_school(self):
        DIGS.gui_setup()
    def display_head(self):
        DIH.gui_setup()
    def display_lab(self):
        DIL.gui_setup()
    def display_school(self):
        DIS.gui_setup()
    def display_union_council(self):
        DIUC.gui_setup()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
