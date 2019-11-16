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
		a, b, c = my_indicator(myoption, i, mystartindex, myendindex, my_cal_length, mydatelist, mydict)

		print('%s\t%.4f\t%.4f\t%.4f\t%.4f\t%d\t%s\t%s\t%s'%
			(mydatelist[i], 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['1. open']), 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['2. high']), 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['3. low']), 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['4. close']), 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['5. volume']),
				a,
				b,
				c))
		

def my_indicator(myoption: str, myindex: int, mystartindex: int, myendindex: int, my_cal_length: int, mydatelist: list, mydict: dict):
	if myoption == 'TR':
		return cal_tr(myindex, mystartindex, my_cal_length, mydatelist, mydict)
	elif myoption == 'MP':
		return cal_moving_average_p(myindex, mystartindex, my_cal_length, mydatelist, mydict)
	elif myoption == 'MV':
		return cal_moving_average_v(myindex, mystartindex, my_cal_length, mydatelist, mydict)	
	elif myoption == 'DP':
		return cal_d_p(myhighthreshold, mylowthreshold, myindex, mystartindex, my_cal_length, mydatelist, mydict)
	elif myoption == 'DV':
		return cal_d_v(myhighthreshold, mylowthreshold, myindex, mystartindex, my_cal_length, mydatelist, mydict)


def cal_tr(myindex: int, mystartindex: int, my_cal_length: int, mydatelist: list, mydict: dict):
	if  ((mystartindex - myindex) < 1):
		return '', '', ''
	elif ((mystartindex - myindex) >= 1):
		temp = 0
		buy_signal = ''
		sell_signal = ''
		today_high = float(mydict['Time Series (Daily)'][mydatelist[myindex]]['2. high']) 
		today_low = float(mydict['Time Series (Daily)'][mydatelist[myindex]]['3. low'])
		yesterday_close = float(mydict['Time Series (Daily)'][mydatelist[myindex+1]]['4. close']) 
		if (today_low < yesterday_close < today_high):
			temp = today_high - today_low
		elif (yesterday_close >= today_high):
			temp = yesterday_close - today_low
		elif (yesterday_close <= today_low):
			temp = today_high - yesterday_close

		tr_value = temp / yesterday_close * 100
		
		if(tr_value <= mybuythreshold):
			buy_signal = 'BUY'
		if(tr_value >= mysellthreshold):
			sell_signal = 'SELL'

		tr_value = '%.2f'%tr_value + "%"

		return tr_value, buy_signal, sell_signal


def cal_moving_average_p(myindex: int, mystartindex: int, my_cal_length: int, mydatelist: list, mydict: dict):

	if  ((mystartindex - myindex) < (my_cal_length-1)):
		return '', '', ''
	elif ((mystartindex - myindex) >= (my_cal_length-1)):
		temp = 0
		prev_temp = 0
		buy_signal = ''
		sell_signal = ''
		for i in range(myindex+9, (myindex - 1), -1):
			temp += float(mydict['Time Series (Daily)'][mydatelist[i]]['4. close'])
			prev_temp += float(mydict['Time Series (Daily)'][mydatelist[i+1]]['4. close'])
		mymovingaverage = temp / my_cal_length
		myyesterdaymovingaverage = prev_temp / my_cal_length
		
		today_close_price = float(mydict['Time Series (Daily)'][mydatelist[myindex]]['4. close'])
		yesterday_close_price = float(mydict['Time Series (Daily)'][mydatelist[myindex+1]]['4. close'])

		if((today_close_price > mymovingaverage) and (yesterday_close_price < myyesterdaymovingaverage)):
			buy_signal = 'BUY'
		if((today_close_price < mymovingaverage) and (yesterday_close_price > myyesterdaymovingaverage)):
			sell_signal = 'SELL'

		return ('%.4f'%mymovingaverage, buy_signal, sell_signal)


def cal_moving_average_v(myindex: int, mystartindex: int, my_cal_length: int, mydatelist: list, mydict: dict):
	if  ((mystartindex - myindex) < (my_cal_length-1)):
		return '', '', ''
	elif ((mystartindex - myindex) >= (my_cal_length-1)):
		temp = 0
		prev_temp = 0
		buy_signal = ''
		sell_signal = ''
		for i in range(myindex+9, (myindex - 1), -1):
			temp += float(mydict['Time Series (Daily)'][mydatelist[i]]['5. volume'])
			prev_temp += float(mydict['Time Series (Daily)'][mydatelist[i+1]]['5. volume'])
		mymovingaverage = temp / my_cal_length
		myyesterdaymovingaverage = prev_temp / my_cal_length

		today_close_price = float(mydict['Time Series (Daily)'][mydatelist[myindex]]['5. volume'])
		yesterday_close_price = float(mydict['Time Series (Daily)'][mydatelist[myindex+1]]['5. volume'])

		if((today_close_price > mymovingaverage) and (yesterday_close_price < myyesterdaymovingaverage)):
			buy_signal = 'BUY'
		if((today_close_price < mymovingaverage) and (yesterday_close_price > myyesterdaymovingaverage)):
			sell_signal = 'SELL'

		return ('%d'%mymovingaverage, buy_signal, sell_signal)


def cal_d_p(myhighthreshold: float, mylowthreshold: float, myindex: int, mystartindex: int, my_cal_length: int, mydatelist: list, mydict: dict):
	if  ((mystartindex - myindex) < (my_cal_length-1)):
		return '', '', ''
	elif ((mystartindex - myindex) >= (my_cal_length-1)):
		temp = 0
		buy_signal = ''
		sell_signal = ''
		for i in range(myindex+9, (myindex - 1), -1):
			if ((float(mydict['Time Series (Daily)'][mydatelist[i]]['4. close']) - float(mydict['Time Series (Daily)'][mydatelist[i+1]]['4. close'])) > 0 ):
				temp += 1
			elif ((float(mydict['Time Series (Daily)'][mydatelist[i]]['4. close']) - float(mydict['Time Series (Daily)'][mydatelist[i+1]]['4. close'])) < 0):
				temp -= 1
		if temp > myhighthreshold:
				buy_signal = 'BUY'
		if temp < mylowthreshold:
				sell_signal = 'SELL'
		return temp, buy_signal, sell_signal
		

def cal_d_v(myhighthreshold: float, mylowthreshold: float, myindex: int, mystartindex: int, my_cal_length: int, mydatelist: list, mydict: dict):
	if  ((mystartindex - myindex) < (my_cal_length-1)):
		return '', '', ''
	elif ((mystartindex - myindex) >= (my_cal_length-1)):
		temp = 0
		buy_signal = ''
		sell_signal = ''
		for i in range(myindex+9, (myindex - 1), -1):
			if ((float(mydict['Time Series (Daily)'][mydatelist[i]]['5. volume']) - float(mydict['Time Series (Daily)'][mydatelist[i+1]]['5. volume'])) > 0 ):
				temp += 1
			elif ((float(mydict['Time Series (Daily)'][mydatelist[i]]['5. volume']) - float(mydict['Time Series (Daily)'][mydatelist[i+1]]['5. volume'])) < 0):
				temp -= 1
		if temp > myhighthreshold:
				buy_signal = 'BUY'
		if temp < mylowthreshold:
				sell_signal = 'SELL'
		return temp, buy_signal, sell_signal



if __name__ == '__main__':
	api_key = pulling_api_key("./api_key.txt")
	mysymbol = input('input your symbol     ')
	mystartdate = input('start date, YYYY-MM-DD ')
	myenddate = input('end date, YYYY-MM-DD ')
	mycommand = input('input your command ')

	try:
		if mycommand.startswith('TR'):
			mylist = mycommand.split(' ')
			myoption = mylist[0]
			mybuythreshold = float(mylist[1])
			mysellthreshold = float(mylist[2])
			# print(myoption, mybuythreshold, mysellthreshold)
		elif(mycommand.startswith('MP')):
			mylist = mycommand.split(' ')
			myoption = mylist[0]
			my_cal_length = int(mylist[1])
			# print(myoption, my_cal_length)
		elif(mycommand.startswith('MV')):
			mylist = mycommand.split(' ')
			myoption = mylist[0]
			my_cal_length = int(mylist[1])
			# print(myoption, my_cal_length)
		elif(mycommand.startswith('DP')):
			mylist = mycommand.split(' ')
			myoption = mylist[0]
			my_cal_length = int(mylist[1])
			myhighthreshold = float(mylist[2][1:])
			mylowthreshold = float(mylist[3][1:])
			# print(myoption, my_cal_length, myhighthreshold, mylowthreshold)
		elif(mycommand.startswith('DV')):
			mylist = mycommand.split(' ')
			myoption = mylist[0]
			my_cal_length = mylist[1]
			myhighthreshold = float(mylist[2][1:])
			mylowthreshold = float(mylist[3][1:])
			# print(myoption, my_cal_length, myhighthreshold, mylowthreshold)
		else:
			print('else condition of mycommand_parse function')
	except:
		print('except of mycommand_parse function')	


	mydict = pull_web_n_store_into_dict(mysymbol)
	mydatelist = create_hash_keys_of_dates_for_cal(mydict)

	mystartindex, myendindex, mydatelength = find_the_length_of_dates(mystartdate, myenddate)
	

	result_outcome(myoption, mystartindex, myendindex, mydatelist, mydict)

	# print(mydatelist)

	# print(mydict['Time Series (Daily)']['2019-11-11'])



	# print(mydict)
	'Just for confirming that I pulled data correctly'
	# print(type(mydict))
	'Just to make sure the data structure is dict'

	# store_dict_into_json_file(mydict)


	
	

	
	
	