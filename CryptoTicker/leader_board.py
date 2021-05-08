from tkinter import *
import tkinter.font as font
from Price_Of_Currency import GetPrice

#declaring the dimensions of the window
Lwindow = Tk()
Lwindow.configure(bg = 'black')
Lwindow.geometry("600x500")


#Setting the page layout
boardfont = font.Font(family = 'Bernard MT Condensed', size = 8, weight = 'bold')
msgfont = font.Font(family = 'Bernard MT Condensed', size = 18, weight = 'bold')
msg = Message(Lwindow,text = 'LEADERBOARDS', font = msgfont, bg = 'black', fg = 'white', width = 280 ).grid(row= 0,column=0)

#name price 24 hourchange 7 day change
def gen_leaderboard():
    from leader_board_logic import sort_value
    from leader_board_logic import ret_str
    data = sort_value()
    Board=''+'{:<15} {:30} {:<30} {:<20}'.format('rank', 'name', 'price', 'Oneday_change', 'oneweek_change')+'\n'
    for i in data:
        rank , name, price, Oneday_change, oneweek_change = i
        Board = Board + '{:<15} {:30} {:<30} {:<20}'.format(rank, name, price, Oneday_change, oneweek_change)+ '\n'

    msg_box = Message(Lwindow, text=Board, bg = 'black' ,fg = 'white', width = 600 ).grid(row = 1, column=0)



Glb_bttn = Button(Lwindow, text = 'Genrate LeaderBoard', bg= 'teal', font = msgfont, fg = 'white', padx = 1, pady = 5, command = gen_leaderboard).grid(row = 2, column = 0)


Lwindow.mainloop()
