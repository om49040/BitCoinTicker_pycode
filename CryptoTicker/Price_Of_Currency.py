from bs4 import BeautifulSoup
import time
import requests
#function to get the real time price of the crypto currencies in rupees
def GetPrice(coin):

    url = 'https://api.lunarcrush.com/v2?data=assets&key=5sz1ekuzs7vygwrux84psk&symbol='+coin
    data = requests.get(url)
    data_jsn = data.json()
    return data_jsn['data'][0]['price']

#Function to take input from the gui interface

    
#if __name__=='__main__':
 #   print(GetPrice('bitcoin'))