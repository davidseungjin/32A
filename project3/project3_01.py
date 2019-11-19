import json
import urllib.request
import requests
from pathlib import Path
from datetime import date

def pulling_api_key(mypath: Path) -> str:
	with open(mypath, 'r') as api:
		key = api.read()
		return key

def pull_web_n_store_into_dict(mysymbol: str) -> dict:
	URL_base = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + mysymbol + '&outputsize=full&apikey=' + api_key
	jsonpage = urllib.request.urlopen(URL_base)
	mycontent = json.loads(jsonpage.read())
	return mycontent

def store_dict_into_json_file(mydict: dict) -> None:
	with open("./myjson.json", 'w') as myjson:
		myjson.write(json.dumps(mycontent))

def create_hash_keys_of_dates_for_cal(mydict: dict) -> list:
	mylist = []
	for i in mydict['Time Series (Daily)'].keys():
		mylist.append(i)
	return mylist

def find_the_length_of_dates(mystartdate: str, myenddate: str) -> int:
	print('mystartdate is ', mystartdate)
	print('myenddate is ', myenddate)
	start_index = 0
	end_index = 0
	for i in range(len(mydatelist)):
		if mydatelist[i] == mystartdate:
			start_index = i
		if mydatelist[i] == myenddate:
			end_index = i
	return start_index, end_index, (start_index - end_index + 1)

def result_outcome(myoption: str, mystartindex: int, myendindex: int, mydatelist: list, mydict: dict) -> None:
	
	print('Date\tOpen\tHigh\tLow\tClose\tVolume\tIndicator\tBuy?\tSell')
	for i in range(mystartindex, (myendindex-1), -1):
		
		
		print('%s\t%.4f\t%.4f\t%.4f\t%.4f\t%d'%
			(mydatelist[i], 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['1. open']), 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['2. high']), 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['3. low']), 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['4. close']), 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['5. volume'])
				), end='\t')
		my1, my2, my3 = my_indicator('MP', i, mystartindex, myendindex, my_cal_length, mydatelist, mydict)
		
		

def my_indicator(myoption: str, myindex: int, mystartindex: int, myendindex: int, my_cal_length: int, mydatelist: list, mydict: dict):
	if myoption == 'TR':
		return '1', '2', '3'
	elif myoption == 'MP':
		my1 = cal_moving_average_p(myindex, mystartindex, my_cal_length, mydatelist, mydict)
		buy_signal = ''
		sell_signal = ''
		today_close_price = float(mydict['Time Series (Daily)'][mydatelist[myindex]]['4. close'])
		yesterday_close_price = float(mydict['Time Series (Daily)'][mydatelist[myindex-1]]['4. close'])

		print('my1 is ', my1)
		print('type is ', type(my1))
		if((today_close_price > my1) and (yesterday_close_price < my1)):
			buy_signal = 'BUY'
		if((today_close_price < my1) and (yesterday_close_price > my1)):
			sell_signal = 'SELL'
		return my1, buy_signal, sell_signal

	elif myoption == 'MV':
		return cal_moving_average_v(myindex, mystartindex, mydatelength, mydatelist, mydict)	
	'''
	What would be options for my_indicator? DP and DV...how to implement?
	elif myoption == 'DP':
		return cal_d_p(myhighthreshold, mylowthreshold, myindex, mystartindex, mydatelength, mydatelist, mydict)
	elif myoption == 'DV':
		pass
	'''


def cal_moving_average_p(myindex: int, mystartindex: int, my_cal_length: int, mydatelist: list, mydict: dict):
	if  ((mystartindex - myindex) < (my_cal_length-1)):
		return ''
	elif ((mystartindex - myindex) >= (my_cal_length-1)):
		temp = 0
		buy_signal = ''
		sell_signal = ''
		for i in range(myindex+9, (myindex - 1), -1):
			temp += float(mydict['Time Series (Daily)'][mydatelist[i]]['4. close'])
		mymovingaverage = temp / my_cal_length
		
		today_close_price = float(mydict['Time Series (Daily)'][mydatelist[myindex]]['4. close'])
		yesterday_close_price = float(mydict['Time Series (Daily)'][mydatelist[myindex+1]]['4. close'])
		return '%.4f'%mymovingaverage

def cal_moving_average_v(myindex: int, mystartindex: int, mydatelength: int, mydatelist: list, mydict: dict):
	if  ((mystartindex - myindex) < (mydatelength-1)):
		return ''
	elif ((mystartindex - myindex) >= (mydatelength-1)):
		temp = 0
		for i in range(mystartindex, (myindex - 1), -1):
			temp += float(mydict['Time Series (Daily)'][mydatelist[i]]['5. volume'])
		return '%.4f'%temp

def cal_d_p(myhighthreshold: float, mylowthreshold: float, myindex: int, mystartindex: int, mydatelength: int, mydatelist: list, mydict: dict):
	if  ((mystartindex - myindex) < (mydatelength-1)):
		return
	elif ((mystartindex - myindex) >= (mydatelength-1)):
		temp = 0
		for i in range(mystartindex, (myindex - 1), -1):
			if ((float(mydict['Time Series (Daily)'][mydatelist[i]]['4. close']) - float(mydict['Time Series (Daily)'][mydatelist[i+1]]['4. close'])) > 0 ):
				temp += 1
			elif ((float(mydict['Time Series (Daily)'][mydatelist[i]]['4. close']) - float(mydict['Time Series (Daily)'][mydatelist[i+1]]['4. close'])) < 0):
				temp -= 1
			else:
				pass
		print('temp is ', temp)
		if(temp >= myhighthreshold):
			return 'BUY'
		elif(temp <= mylowthreshold):
			return 'SELL'
		else:
			return ''
		




if __name__ == '__main__':
	api_key = pulling_api_key("./api_key.txt")
	mysymbol = input('input your symbol     ')
	mystartdate = input('start date, YYYY-MM-DD ')
	myenddate = input('end date, YYYY-MM-DD ')
	# mycommand = input('input your command ')
	

	# dd/mm/YY
	# d1 = today.strftime("%d/%m/%Y")
	# print("d1 =", d1)

	mydict = pull_web_n_store_into_dict(mysymbol)
	mydatelist = create_hash_keys_of_dates_for_cal(mydict)

	mystartindex, myendindex, mydatelength = find_the_length_of_dates(mystartdate, myenddate)
	
	my_cal_length = 10
	myoption = 'MP'
	mytoday = date.today()
	

	# print(mystartindex)
	# print(myendindex)
	# print(mydatelength)

	result_outcome(myoption, mystartindex, myendindex, mydatelist, mydict)

	# print(mydatelist)

	# print(mydict['Time Series (Daily)']['2019-11-11'])



	# print(mydict)
	'Just for confirming that I pulled data correctly'
	# print(type(mydict))
	'Just to make sure the data structure is dict'

	# store_dict_into_json_file(mydict)


	
	

	
	
	