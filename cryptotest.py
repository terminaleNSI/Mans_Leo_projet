from pycoingecko import CoinGeckoAPI
import time
cg = CoinGeckoAPI()

print(cg.ping())
ide = cg.get_coins_list()[0]['id']
#print(cg.get_exchanges_list())

actuel_time = time.time()
time_1h = actuel_time - (86400/24)
time_24h = actuel_time - (86400)
time_7j = actuel_time - (86400*7)
time_31j= actuel_time - (86400*31)
btc1h= cg.get_coin_market_chart_range_by_id('bitcoin', 'usd',time_24h,actuel_time)
#btc7j= cg.get_coin_market_chart_range_by_id('bitcoin', 'usd',time_7j,actuel_time)
#btc31j= cg.get_coin_market_chart_range_by_id('bitcoin', 'usd',time_31j,actuel_time)


#print("Le bitcoin vaut : "+str(int(btc1h["prices"][87][1]))+"$ il valait : "+str(int(btc7j["prices"][168][1]))+"$ il y a 7 jour, et il valait "+str(int(btc31j["prices"][720][1])) +"$ il y a un mois.")
timee = 5
for i in btc1h["prices"] :
    print("Bitcoin il y a "+str(timee)+" min ="+str(int(i[1]))+"$")
    timee+=5