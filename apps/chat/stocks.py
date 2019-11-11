import urllib
import urllib.request
import os
import csv
from random import randint

def get_stock_price(user_id, stock_code):
	stock_url = 'https://stooq.com/q/l/?s=' + stock_code + '&f=sd2t2ohlcv&h&e=csv'
	name = str(user_id) + 'output' + str(randint(0,100)) + '.csv'
	urllib.request.urlretrieve(stock_url, name)
	csv_file = open(name)
	csv_reader = csv.reader(csv_file, delimiter=',')
	header = next(csv_reader)
	content = next(csv_reader)
	name_stock = content[0]
	close_price = content[-2]
	output_text = (name_stock + " quote is $" + close_price + " per share") if close_price != 'N/D' else ('Stock code not valid')
	csv_file.close()
	os.remove(name)
	return output_text