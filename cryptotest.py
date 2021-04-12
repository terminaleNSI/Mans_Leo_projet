from pycoingecko import CoinGeckoAPI
import time
""" Initialisation de l'API """

cg = CoinGeckoAPI()
#print(cg.ping())

""" Mise en place du systeme de temps (en valeur UNIX) """
actuel_time = time.time()
time_1h = actuel_time - (86400/24)
time_24h = actuel_time - (86400)
time_7j = actuel_time - (86400*7)
time_31j= actuel_time - (86400*31)


a2234 = cg.get_exchanges_list()
liste_monnaies = cg.get_coins_list() # Liste de toute les cryptomonnaies
liste_type_monnaies = cg.get_supported_vs_currencies() # liste des types de monnaie(eur,usd,btc)
info_globale = cg.get_global() # information globale sur les crypto
#price = cg.get_price()

btc1h= cg.get_coin_market_chart_range_by_id('bitcoin', 'usd',0,actuel_time)
btc = cg.get_coin_by_id("01coin")

""" Mise en place d'une liste contenant les informations principales"""

informations = []
for i in liste_monnaies[29:] :
    try :
        prixMois = cg.get_coin_market_chart_range_by_id(i["id"],'usd',time_31j,actuel_time)
        prixJour = cg.get_coin_market_chart_range_by_id(i["id"],'usd',time_24h,actuel_time)
        image  = cg.get_coin_by_id(i["id"])["image"]
        dico ={"Nom" : i["name"], "Prix_Mois($)" : prixMois,"Prix_Jour($)" : prixJour,"Image" : image }
        informations.append(dico)
    except : 
        pass