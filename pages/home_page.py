from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as ct
from random import choice
import database as dbf

import customtkinter as ct
import sys

class HomeFrame(ct.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, bg_color="blue")
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1), weight=1)
        self.table = None
        self.register().grid(row=0, columnspan=2, sticky="nswe")
        self.table_view().grid(row=1, columnspan=2, sticky="nswe")
        self.table.bind('<ButtonRelease>', self.display_data)
        self.insert_data()
        self.logo()
        self.pack()
    def register(self):
        global text, count, reg_title, name_entry, level_entry, team_points_entry, quiz_points_entry,improv_points_entry, act_points_entry
        text = ''
        count = 0
        register_frame = ct.CTkFrame(self, fg_color="transparent")
        reg_title = ct.CTkLabel(
            register_frame,
            text="Register Player",
            font=("Roboto", 25, "bold"),
            bg_color="transparent",
            text_color="#7196DE",
            fg_color="transparent",
        )
        name_label = ct.CTkLabel(
            register_frame,
            text="Name:",
            font=( "Roboto",18),
            cursor="hand2",  # Set cursor to "hand2" to indicate clickable button
        )
        level_label = ct.CTkLabel(
            register_frame,
            text="Level:",
            font=( "Roboto",18),
            cursor="hand2",  # Set cursor to "hand2" to indicate clickable button
        )
        name_entry = ct.CTkEntry(
            register_frame,
            placeholder_text="Enter name"
        )
        level_entry = ct.CTkEntry(
            register_frame,
            placeholder_text="Enter tennis level"
        )
        message_label = ct.CTkLabel(
            register_frame,
            text="PS: Select a row \n    to delete or update",
            font=( "Roboto",15),
            cursor="hand2",
            width=10
        )
        
        add_button = ct.CTkButton(
            register_frame,
            width=80,
            text="Add",
            height=30,
            fg_color="#585656",
            font=("Roboto", 14),
            cursor="hand2",
            command=self.insert
        )
        delete_button = ct.CTkButton(
            register_frame,
            width=80,
            text="Delete",
            height=30,
            fg_color="#585656",
            cursor="hand2",
            font=("Roboto", 14),
            command=self.delete
        )
        update_button = ct.CTkButton(
            register_frame,
            width=80,
            text="Update",
            height=30,
            fg_color="#585656",
            font=("Roboto", 14),
            cursor="hand2",
            command=self.update
        )
        clear_button = ct.CTkButton(
            register_frame,
            width=80,
            text="Clear",
            height=30,
            fg_color="#585656",
            font=("Roboto", 14),
            cursor="hand2",
            command=self.clear
        )
        tracker_title = ct.CTkLabel(
            self,
            text="Tracker data",
            font=("Roboto", 22, "bold"),
        )
        team_points_label = ct.CTkLabel(
            register_frame,
            text="Team points:",
            font=( "Roboto",16),
            cursor="hand2",  # Set cursor to "hand2" to indicate clickable button
        )
        team_points_entry = ct.CTkEntry(
            register_frame,
            placeholder_text="Enter points",
            font=( "Roboto",12),
        )

        quiz_points_label = ct.CTkLabel(
            register_frame,
            text="Quiz points:",
            font=( "Roboto",16),
            cursor="hand2",  # Set cursor to "hand2" to indicate clickable button
        )
        quiz_points_entry = ct.CTkEntry(
            register_frame,
            placeholder_text="Enter points",
            font=( "Roboto",12),
        )
        act_points_label = ct.CTkLabel(
            register_frame,
            text="Activity points:",
            font=( "Roboto",16),
            cursor="hand2",  # Set cursor to "hand2" to indicate clickable button
        )
        act_points_entry = ct.CTkEntry(
            register_frame,
            placeholder_text="Enter points",
            font=( "Roboto",12),
        )
        improv_points_label = ct.CTkLabel(
            register_frame,
            text="Improvement points:",
            font=( "Roboto",16),
            cursor="hand2",  # Set cursor to "hand2" to indicate clickable button
        )
        improv_points_entry = ct.CTkEntry(
            register_frame,
            placeholder_text="Enter points",
            font=( "Roboto",12),
        )

        reg_title.place(x=35,y=30)
        name_label.place(x=35, y=75)
        level_label.place(x=200, y=75)
        name_entry.place(x=35,y=110)
        level_entry.place(x=200,y=110)
        team_points_label.place(x=35, y=148)
        team_points_entry.place(x=35, y=180)
        quiz_points_label.place(x=200, y=148)
        quiz_points_entry.place(x=200, y=180)
        act_points_label.place(x=365, y=75)
        act_points_entry.place(x=365, y=110)
        improv_points_label.place(x=365, y=148)
        improv_points_entry.place(x=365, y=180)
        add_button.place(x=300,y=30)
        delete_button.place(x=400,y=30)
        update_button.place(x=500,y=30)
        clear_button.place(x=600,y=30)
        #message_label.place(x=500, y= 110)
        #self.slider()
        
        return register_frame
    def insert(self):
        name = name_entry.get()
        level = level_entry.get()
        team_points = team_points_entry.get()
        quiz_points = quiz_points_entry.get()
        improv_points = improv_points_entry.get()
        act_points = act_points_entry.get()

        if not(name and level):
            messagebox.showerror("Errror", "enter all fields")
        elif dbf.name_exists(name):
            messagebox.showerror("Error", "Name aleready exists")
        else:
            try:
                team_points = int(team_points)
                quiz_points = int(quiz_points)
                improv_points = int(improv_points)
                act_points = int(act_points)
                dbf.insert_players(name,level,team_points,quiz_points,act_points, improv_points)
                self.insert_data()
                self.clear()
                #self.ordertable
                messagebox.showinfo("Success", "Data has been inserted")
            except ValueError:
                messagebox.showerror("Error", "Points should be an integer")
    def clear(self, *clicked):
        if clicked:
            self.table.selection_remove(self.table.focus())
            self.table.focus("")
        name_entry.delete(0,"end")
        level_entry.delete(0,"end")
        quiz_points_entry.delete(0,"end")
        act_points_entry.delete(0,"end")
        improv_points_entry.delete(0,"end")
        team_points_entry.delete(0,"end")
    def display_data(self, event):
        global name_entry, level_entry, team_points_entry, quiz_points_entry, act_points_entry, improv_points_entry
        selected_item = self.table.focus()
        if selected_item:
            row = self.table.item(selected_item)['values']
            self.clear()
            name_entry.insert(0, row[0])
            level_entry.insert(0, row[1])
            team_points_entry.insert(0, row[2])
            quiz_points_entry.insert(0,row[3])
            act_points_entry.insert(0,row[4])
            improv_points_entry.insert(0,row[5])
        else:
            pass
    def update(self):
        selected_item = self.table.focus()
        if not selected_item:
            messagebox.showerror("Error", "Choose a player to update")
        else:
            name = name_entry.get()
            level = level_entry.get()
            team_points = team_points_entry.get()
            quiz_points = quiz_points_entry.get()
            improv_points = improv_points_entry.get()
            act_points = act_points_entry.get()

            if not(name and level):
                messagebox.showerror("Errror", "enter all fields")
            else:
                try:
                    team_points = int(team_points)
                    quiz_points = int(quiz_points)
                    improv_points = int(improv_points)
                    act_points = int(act_points)
                    dbf.update_players(name, level,team_points,quiz_points, act_points, improv_points)

                    self.table.delete(*self.table.get_children())

                    self.insert_data()

                    self.clear()
                    messagebox.showinfo("Success", "Data has been updated")
                except ValueError:
                    messagebox.showerror("Error", "Points should be an integer")
    def delete(self):
        selected_item = self.table.focus()
        if not selected_item:
             messagebox.showerror("error", "Choose a product to delete")
        else:
            name = name_entry.get()
            dbf.delete_players(name)
            self.clear()
            self.table.delete(*self.table.get_children())
            self.insert_data()

                
    def slider(self):
        global text, count

        def update_label():
            global text, count
            if count < len(reg_title.cget("text")):
                text += reg_title.cget("text")[count]
                count += 1
                reg_title.configure(text=text)
                reg_title.after(200, update_label)
                print("hello")
                print(count)
                count+=1

        update_label()


    def table_view(self):
        table_frame = ct.CTkFrame(self, fg_color="transparent")
        # Create the Treeview widget
        self.table = ttk.Treeview(
            table_frame,
            columns=('Name', "Level", "Team points", "Quiz points", "Activity Points", "Improvement points"),
            show='headings',
            height=12,
        )

        # Define the headings
        self.table.heading('Name', text='First name')
        self.table.heading('Level', text='Level')
        self.table.heading('Team points', text='Team points')
        self.table.heading('Quiz points', text='Quiz points')
        self.table.heading('Activity Points', text='Activity Points')
        self.table.heading('Improvement points', text='Improvement points')

        style = ttk.Style()
# set ttk theme to "clam" which support the fieldbackground option
        style.theme_use("clam")
        style.configure("Treeview", background="#333030", 
                        fieldbackground="#333030", foreground="white")

        # Configure the styles for headings and columns

        x_scrollbar = ttk.Scrollbar(table_frame, orient='horizontal', command=self.table.xview)
        self.table.configure(xscrollcommand=x_scrollbar.set)

        x_scrollbar.pack(side='bottom', fill='x')
        self.table.pack(side="bottom", pady=20, padx=20)
        
        return table_frame
    
    def insert_data(self):
        if self.table:  # Check if self.table is not None
            self.table.delete(*self.table.get_children())  # Clear existing data
        players = dbf.fetch_players()
        for player in players:
            self.table.insert("", "end", values=player)

    def logo(self):
    # Open the original image
        original_image = Image.open('./images/logo.png')

        # Resize the image to the desired height and width
        desired_width = 150  # Change this to the desired width
        desired_height = 150  # Change this to the desired height
        resized_image = original_image.resize((desired_width, desired_height), Image.LANCZOS)

        # Convert the resized image to PhotoImage
        logo_image = ImageTk.PhotoImage(resized_image)

        # Create the CTkLabel with the resized image
        logo_label = ct.CTkLabel(
            self,
            image=logo_image,
            fg_color="transparent",
            bg_color="transparent",
            text=''
        )

        logo_label.image = logo_image  # Keep a reference to avoid garbage collection
        logo_label.place(x=530, y=90)



        