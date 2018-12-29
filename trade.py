"""
	algorithm
	- find the 
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup


class CMC(object):
	"""docstring for CMC"""
	def __init__(self):
		cmc_url = "https://coinmarketcap.com/"
		cmc_html = r"C:\Users\TAN\Desktop\Cryptocurrency Market Capitalizations _ CoinMarketCap.html"
		cmc_page = requests.get(cmc_url)
		# df_list = pd.read_html(cmc_page.content)
		df_list = pd.read_html(cmc_html)
		df_100 = df_list[0]
		df_100['change_percent'] = pd.to_numeric(df_100['Change (24h)'].str.replace("%",""))
		# print(df_100['change_percent'])
		df_100 = df_100.sort_values('change_percent')
		print(df_100)
		


CMC()