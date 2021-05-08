import requests

Allcoin=['BTC','LTC','ETH','BNB','DOGE','XRP','USDT','ADA','DOT','BCH','UNI','LINK']

#Function for collecting the data: name price 24 hourchange 7 day change

def get_data(coin):
    url = 'https://api.lunarcrush.com/v2?data=assets&key=5sz1ekuzs7vygwrux84psk&symbol='+coin
    data = requests.get(url)
    data_jsn = data.json()
    return [data_jsn['data'][0]['id'],data_jsn['data'][0]['name'],data_jsn['data'][0]['price'],data_jsn['data'][0]['percent_change_24h'],data_jsn['data'][0]['percent_change_7d']]

def skey(a):
    return a[0]

def ret_str(a):
    return str(a[0])+'\t'+a[1]+'\t'+str(a[2])+'\t'+str(a[3])+'\t'+str(a[4])

def sort_value():
    all_data=[]
    #the for loop will add all the data to the list
    for i in Allcoin:
        all_data.append(get_data(i))
    all_data.sort(key = skey)
    return all_data

