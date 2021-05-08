from tkinter import *
import tkinter.font as font
from time import sleep

root = Tk()
root.configure(bg = 'light blue')
root.geometry("600x500")
#defining the area to show output
e=Entry(root, bg ='light green', width = 20, borderwidth = 5, font=('calibre',22, 'bold'))
e.place(x = 130, y=300 )

#functions when the buttons are clicked
def bttn_clicked(crypto):
    import Price_Of_Currency as pc
    e.delete(0,END)
    e.insert(0,str(pc.GetPrice(crypto))+" $")

def leader_boards():
    import leader_board
# Buttons for the gui
buttonFont = font.Font(family='Helvetica', size=16, weight='bold')
BitCoin_bttn = Button(root, font = buttonFont, bg='teal',fg='white', text = 'Bitcoin', padx=40 , pady=5, command = lambda: bttn_clicked('BTC')).grid(row = 0 , column = 0)
LitCoin_bttn= Button(root, font = buttonFont, bg='ORANGE',fg='white', text = 'Litecoin', padx=35 , pady=5, command = lambda: bttn_clicked('LTC')).grid(row = 1, column =0)
Ethereum_bttn= Button(root, font = buttonFont, bg='blue',fg='white', text = 'Ethereumcoin', padx=4 , pady=5, command = lambda: bttn_clicked('ETH')).grid(row = 2, column =0)
Binance_bttn= Button(root, font = buttonFont, bg='light blue',fg='white', text = 'Binance', padx=12 , pady=5, command = lambda: bttn_clicked('BNB')).grid(row = 0, column =1)
Doge_bttn= Button(root, font = buttonFont, bg='dark green',fg='white', text = 'Dogecoin', padx=5 , pady=5, command = lambda: bttn_clicked('DOGE')).grid(row = 1, column = 1)
Xrp_bttn= Button(root, font = buttonFont, bg='grey',fg='white', text = 'XRP', padx=33 , pady=5, command = lambda: bttn_clicked('XRP')).grid(row = 2, column = 1)
Tether_bttn= Button(root, font = buttonFont, bg='black',fg='white', text = ' Tethercoin ', padx=12 , pady=5, command = lambda: bttn_clicked('USDT')).grid(row = 0, column =2 )
Cardano_bttn= Button(root, font = buttonFont, bg='magenta',fg='white', text = ' Cardanocoin ', padx=2 , pady=5, command = lambda: bttn_clicked('ADA')).grid(row = 1, column =2 )
Polkadot_bttn= Button(root, font = buttonFont, bg='red',fg='white', text = 'Polkadotcoin', padx=5 , pady=5, command = lambda: bttn_clicked('DOT')).grid(row = 2, column =2 )
Bitcoincash_bttn= Button(root, font = buttonFont, bg='magenta',fg='white', text = 'Bitcoincash ', padx=5 , pady=5, command = lambda: bttn_clicked('BCH')).grid(row = 0, column =3 )
Uniswap_bttn= Button(root, font = buttonFont, bg='maroon',fg='white', text = '   Uniswap   ', padx=5 , pady=5, command = lambda: bttn_clicked('UNI')).grid(row = 1, column =3 )
Chainlink_bttn= Button(root, font = buttonFont, bg='blue',fg='white', text = '  Chainlink  ', padx=5 , pady=5, command = lambda: bttn_clicked('LINK')).grid(row = 2, column =3 )

lb_bttn = Button(root, text = 'LeaderBoard', bg= 'green', font = buttonFont, fg = 'white', padx = 1, pady = 5,command = leader_boards).place(x = 470, y =300)




#The program runs from here
root.mainloop()