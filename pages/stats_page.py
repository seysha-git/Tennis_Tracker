from tkinter import messagebox
import tkinter as  tk
from PIL import Image, ImageTk
import tkinter as ct
from random import choice
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import database as dbf
from collections import Counter


import customtkinter as ct
import sys
class StatsFrame(ct.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=5)
        self.rowconfigure(2, weight=2)
        self.columnconfigure((0,1,2), weight=1)
        self.quiz_leader().grid(row=0, column=0, sticky="nswe")
        self.team_leader().grid(row=0, column=1, sticky="nswe")
        self.act_leader().grid(row=0, column=2, sticky="nswe")
        self.level_distribution().grid(row=1, column=2, sticky="nswe")

        ct.CTkLabel(self,bg_color="#272B34", text="y", font=('Bold', 30)).grid(rowspan=1, columnspan=2, sticky="nswe")
        #ct.CTkLabel(self, bg_color="yellow", text="x", font=('Bold', 30)).grid(row=1, column=2, sticky="nswe")
        self.top_scores().grid(row=2, columnspan=2, sticky="nswe")

        """
        ct.CTkLabel(self, bg_color="red", text="x", font=('Bold', 30)).grid(row=0, column=0, sticky="nswe")
        ct.CTkLabel(self, bg_color="blue", text="x", font=('Bold', 30)).grid(row=0, column=1, sticky="nswe")
        ct.CTkLabel(self, bg_color="green", text="x", font=('Bold', 30)).grid(row=0, column=2, sticky="nswe")
        ct.CTkLabel(self, bg_color="blue", text="y", font=('Bold', 30)).grid(row=1, columnspan=2, sticky="nswe")
        ct.CTkLabel(self, bg_color="yellow", text="x", font=('Bold', 30)).grid(row=1, column=2, sticky="nswe")
        ct.CTkLabel(self, bg_color="red", text="x", font=('Bold', 30)).grid(row=2, columnspan=2, sticky="nswe")
        """

        self.pack()
    def quiz_leader(self):
        players = dbf.fetch_players()
        points = []
        for player in players:
            quiz_points = player[3]
            points.append(quiz_points)
        max_score = self.find_highest_score(points)
        player_name = dbf.find_player(max_score)[0]
        ql_frame = ct.CTkFrame(self, fg_color="transparent", bg_color="#10141B", height=50)
        original_image = Image.open('./images/1st_place.png')
        width = 50
        height = 50
        points = 200
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        title_label = ct.CTkLabel(self, text="Quiz Leader", text_color="#7196DE", font=("Roboto Medium", 20, "bold"), bg_color="#10141B")
        player_label = ct.CTkLabel(self, text=f"{player_name}, {max_score} pts", font=("Roboto", 17, "bold"), bg_color="#10141B")
        place_img = ImageTk.PhotoImage(resized_image)
        place_label = ct.CTkLabel(
            self,
            image=place_img,
            fg_color="transparent",
            bg_color="#10141B",
            text=''
        )

        place_label.image = place_img  # Keep a reference to avoid garbage collection
        title_label.place(x=30, y=8)
        place_label.place(x=25, y=44)
        player_label.place(x=78, y=46)

        return ql_frame
    def team_leader(self):
        players = dbf.fetch_players()
        points = []
        for player in players:
            quiz_points = player[2]
            points.append(quiz_points)
        max_score = self.find_highest_score(points)
        player_name = dbf.find_player(max_score)[0]

        tl_frame = ct.CTkFrame(self, fg_color="transparent", height=50, bg_color="#1F2124")
        original_image = Image.open('./images/1st_place.png')
        width = 50
        height = 50
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        title_label = ct.CTkLabel(self, text="Team Leader", text_color="#7196DE", font=("Roboto Medium", 20, "bold"), bg_color="#1F2124")
        player_label = ct.CTkLabel(self, text=f"{player_name}, {max_score} pts", font=("Roboto", 17, "bold"), bg_color="#1F2124")
        place_img = ImageTk.PhotoImage(resized_image)
        place_label = ct.CTkLabel(
            self,
            image=place_img,
            fg_color="transparent",
            bg_color="#1F2124",
            text=''
        )

        place_label.image = place_img  # Keep a reference to avoid garbage collection
        title_label.place(x=250, y=8)
        place_label.place(x=240, y=44)
        player_label.place(x=290, y=46)
        return tl_frame
    def act_leader(self):
        players = dbf.fetch_players()
        points = []
        for player in players:
            quiz_points = player[4]
            points.append(quiz_points)
        max_score = self.find_highest_score(points)
        player_name = dbf.find_player(max_score)[0]
        al_frame = ct.CTkFrame(self, fg_color="transparent",bg_color="#272B34", height=50, corner_radius=20)
        original_image = Image.open('./images/1st_place.png')
        width = 50
        height = 50
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        title_label = ct.CTkLabel(self, text="Activity Leader", text_color="#7196DE", font=("Roboto Medium", 20, "bold"), bg_color="#272B34")
        player_label = ct.CTkLabel(self, text=f"{player_name}, {max_score} pts", font=("Roboto", 17, "bold"), bg_color="#272B34")
        place_img = ImageTk.PhotoImage(resized_image)
        place_label = ct.CTkLabel(
            self,
            image=place_img,
            fg_color="transparent",
            bg_color="#272B34",
            text=''
        )

        place_label.image = place_img  # Keep a reference to avoid garbage collection
        title_label.place(x=500, y=8)
        place_label.place(x=490, y=44)
        player_label.place(x=540, y=46)
        return al_frame
    def level_distribution(self):
        lvl_frame = ct.CTkFrame(self, fg_color="transparent", bg_color="#1B1E24", height=65)
        title_label = ct.CTkLabel(lvl_frame, text="Level Distribution", bg_color="#1B1E24", font=("Roboto Medium", 20, "bold"), text_color="#7196DE")
        players = dbf.fetch_players()
        levels = [player[1] for player in players]
        counter = Counter(levels)
        level_types = counter.keys()
        amount = counter.values()
        colors = ['orange', 'green', 'yellow', 'red']
        fig, ax = plt.subplots(figsize=(4,3))
        wedges, texts, autotexts = ax.pie(amount, labels=level_types, autopct="%1.1f%%", shadow=True, wedgeprops={'alpha': 1}, colors=colors)
        for text in texts:
            text.set_color("white")
            text.set_fontsize("large")
        for at in autotexts:
            at.set_fontsize("large")
        fig.set_facecolor('#1B1E24')
        # Create the pie frame with a smaller size
        pie_frame = ct.CTkFrame(lvl_frame,fg_color="transparent", bg_color="#1B1E24")
        pie_frame.pack(anchor="center")  # Adjust the row and column as needed
        canvas_pie = FigureCanvasTkAgg(fig, master=pie_frame)
        canvas_pie.draw()
        # Use the place method to move the pie chart down within the pie_frame
        canvas_pie.get_tk_widget().pack() # Adjust the x and y values as needed
        pie_frame.place(x=-33, y=38)
        title_label.pack(pady=17)
        return lvl_frame
    def top_scores(self):
        lb_frame = ct.CTkFrame(self, fg_color="transparent", bg_color="#12161F", height=40, width=100)
        title_label = ct.CTkLabel(lb_frame, bg_color="#12161F", text="Top scores", font=("Roboto", 20, "bold"), text_color="#7196DE")

        original_image = Image.open('./images/1st_place.png')
        width = 30
        height = 30
        resized_image = original_image.resize((width, height), Image.LANCZOS)
        place_img = ImageTk.PhotoImage(resized_image)
        place_label = ct.CTkLabel(
            lb_frame,
            image=place_img,
            fg_color="transparent",
            bg_color="#12161F",
            text=''
        )

        place_label.image = place_img 

        players = dbf.fetch_players()
        # Sort players based on their total points in descending order
        players.sort(key=lambda player: sum(player[2:]), reverse=True)

        # Take the top 3 players and their corresponding total points
        top_players = players[:3]
        top_names = [player[0] for player in top_players]
        total_points = [sum(player[2:]) for player in top_players]
        title1_label = ct.CTkLabel(lb_frame, text=f"{top_names[0]} is leading by {total_points[0]-total_points[1]} points !!", text_color="#7196DE", font=("Roboto Medium", 15, "bold"), bg_color="#12161F")

        fig, ax = plt.subplots(figsize=(6, 1))
        bars = ax.barh(top_names, total_points, edgecolor='none', height=0.8)
        #ax.set_ylabel("Players", color='white')
        #ax.set_xlabel("Total points", color='white')
        ax.tick_params(axis='y', colors='white')
        ax.set_frame_on(False)

        bar_frame = ct.CTkFrame(lb_frame, fg_color="#12161F", bg_color="#12161F")
        bar_frame.pack(anchor="center")
        fig.set_facecolor('#12161F')
        ax.set_facecolor('#12161F')

        for i, bar in enumerate(bars):
            ax.annotate(f"{total_points[i]} pts", xy=(bar.get_width() - 0.5, bar.get_y() + bar.get_height() / 2),
                xytext=(0, 0), textcoords='offset points', color='white', va='center', ha='right', fontsize=9)

        bar_graph = FigureCanvasTkAgg(fig, master=bar_frame)
        bar_graph.draw()
        bar_graph.get_tk_widget().pack()
        title_label.place(x=25,y=10)
        place_label.place(x=175, y=10)
        title1_label.place(x=205,y=10)
        bar_frame.place(x=10,y=40)
        return lb_frame
    def find_highest_score(self,arr):
        minimum = arr[0]
        for el in arr:
            if minimum < el:
                minimum = el
        return minimum


