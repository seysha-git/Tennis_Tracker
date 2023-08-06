import tkinter
import tkinter.messagebox
import customtkinter as ct
import sys
#import pages
from pages import home_page, stats_page


ct.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("blue") 

class App(ct.CTk):
    def __init__(self, size, title):
        super().__init__()
        self.title(title)
        self.x =self.winfo_screenwidth()//5
        self.y = int(self.winfo_screenheight()*0.15)
        self.geometry(f'{size[0]}x{size[1]}+' + str(self.x) + '+' + str(self.y))
        self.resizable(False, False)
        self.sidebar = SideBar(self, size[1], self.show_home_page, self.show_stats_page, self.show_pred_page, self.show_learn_page)
        self.mainframe = MainFrame(self)
        self.show_home_page()
        self.mainloop()
    def show_home_page(self):
        self.mainframe.show_page(self.mainframe.home_page)
    def show_stats_page(self):
        self.mainframe.show_page(self.mainframe.stats_page)
    def show_pred_page(self):
        self.mainframe.show_page(self.mainframe.pred_page)
    def show_learn_page(self):
        self.mainframe.show_page(self.mainframe.learn_page)

class SideBar(ct.CTkFrame):
    def __init__(self,parent, height, show_home_page, show_stats_page, show_preds_page, show_learn_page):
        super().__init__(parent, width=200,height=height, corner_radius=0)
        self.show_home_page = show_home_page
        self.show_stats_page = show_stats_page
        self.show_preds_page = show_preds_page
        self.show_learn_page = show_learn_page
        self.pack(side="left")
        self.pack_propagate(False)
        self.side_layout()
    def side_layout(self):
        self.side_title().place(x=-3, y=55)
        self.home_btn().place(x=25, y=170)
        self.stats_btn().place(x=25, y=270)
        self.prediction_btn().place(x=25, y=370)
        self.learn_btn().place(x=25, y=470)
        
    def side_title(self):
        side_title = ct.CTkLabel(
            self,
            text="   Summercamp \ntracker 2023",
            width=0,
            text_color="#7196DE",
            font=("Roboto", 25, "bold")
        )
        return side_title
    def home_btn(self):
        global home_btn
        home_btn = ct.CTkLabel(
            self,
            text='Home',
            font=( "Roboto Medium",22),
            cursor="hand2",  # Set cursor to "hand2" to indicate clickable button
        )
        home_btn.bind("<Button-1>", lambda e: self.show_home_page())
        return home_btn
    def stats_btn(self):
        global stats_btn
        stats_btn = ct.CTkLabel(
            self,
            text='Players Stats',
            font=( "Roboto Medium",22),
            cursor="hand2",  # Set cursor to "hand2" to indicate clickable button
        )
        stats_btn.bind("<Button-1>", lambda e: self.show_stats_page())
        return stats_btn
    def prediction_btn(self):
        global prediction_btn
        prediction_btn = ct.CTkLabel(
            self,
            text='Predictions',
            font=( "Roboto Medium",22),
            cursor="hand2",  # Set cursor to "hand2" to indicate clickable button
        )
        prediction_btn.bind("<Button-1>", lambda e:self.show_preds_page())
        return prediction_btn
    def learn_btn(self):
        global learn_btn
        learn_btn = ct.CTkLabel(
            self,
            text='Learn more',
            font=( "Roboto Medium",22),
            cursor="hand2",  # Set cursor to "hand2" to indicate clickable button
        )
        learn_btn.bind("<Button-1>", lambda e: self.show_learn_page())
        return learn_btn
class MainFrame(ct.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent, width=700, height=660)
        self.pack(side="top", pady=60)
        self.pack_propagate(False)
    def show_page(self, page_func):
        for widget in self.winfo_children():
            widget.destroy()
        page_frame = page_func()
        page_frame.pack(fill='both', expand=True)
    def home_page(self):
        home_frame = home_page.HomeFrame(self)
        return home_frame

    def stats_page(self):
        stats_frame = stats_page.StatsFrame(self)
        return stats_frame

    def pred_page(self):
        pred_frame = ct.CTkFrame(self)
        lb = ct.CTkLabel(pred_frame, text='pred page \n Page: 3', font=('Bold', 30))
        lb.pack()
        return pred_frame

    def learn_page(self):
        learn_frame = ct.CTkFrame(self)
        lb = ct.CTkLabel(learn_frame, text='Learn More page \n Page: 4', font=('Bold', 30))
        lb.pack()
        return learn_frame


        




App((1000, 600), "Summercamp project")
