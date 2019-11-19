import json
import urllib.request
import requests
from pathlib import Path
from datetime import date
# from project3_03_related import pulling_api_key
# from project3_03_related import pull_web_n_store_into_dict
# from project3_03_related import store_dict_into_json_file
# from project3_03_related import create_hash_keys_of_dates_for_cal
# from project3_03_related import find_the_length_of_dates

def pulling_api_key(mypath: Path) -> str:
	with open(mypath, 'r') as api:
		key = api.read()
		return key

def pull_web_n_store_into_dict(mysymbol: str, api_key) -> dict:
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


def result_outcome(myoption) -> None:
	print('Date\tOpen\tHigh\tLow\tClose\tVolume\tIndicator\tBuy?\tSell')
	for i in range(mystartindex, (myendindex-1), -1):
		# print('myoption is ', myoption)
		indicator, buy, sell = run_indicator(my_option(myoption), i)

		print('%s\t%.4f\t%.4f\t%.4f\t%.4f\t%d\t%s\t%s\t%s'%
			(mydatelist[i], 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['1. open']), 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['2. high']), 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['3. low']), 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['4. close']), 
				float(mydict['Time Series (Daily)'][mydatelist[i]]['5. volume']),
				indicator, buy, sell
				))

def my_option(myoption) -> 'Class':
	if myoption == 'TR':
		return TR()
	if myoption == 'MP':
		return MP()
	if myoption == 'MV':
		return MV()
	if myoption == 'DP':
		return DP()
	if myoption == 'DV':
		return DV()
	

def run_indicator(myclass: 'Class', myindex):
	_indicator = myclass.cal_indicator(myindex)
	_buy = myclass.cal_buy(myindex)
	_sell = myclass.cal_sell(myindex)
	return _indicator, _buy, _sell


class TR:
	def cal_indicator(self, myindex):
		if  ((mystartindex - myindex) < 1):
			self._truevalue = 0
			self._indicator = ''
		elif ((mystartindex - myindex) >= 1):
			temp = 0
			today_high = float(mydict['Time Series (Daily)'][mydatelist[myindex]]['2. high']) 
			today_low = float(mydict['Time Series (Daily)'][mydatelist[myindex]]['3. low'])
			yesterday_close = float(mydict['Time Series (Daily)'][mydatelist[myindex+1]]['4. close']) 
			if (today_low < yesterday_close < today_high):
				temp = today_high - today_low
			elif (yesterday_close >= today_high):
				temp = yesterday_close - today_low
			elif (yesterday_close <= today_low):
				temp = today_high - yesterday_close
			self._truevalue = temp / yesterday_close * 100
			self._indicator = '%.2f'%(self._truevalue) + '%'
		return self._indicator
	def cal_buy(self, myindex):
		self._buy = '\t'
		if((mystartindex - myindex) < 1):
			return self._buy	
		else:
			if((self._truevalue) < float(mybuy[1:])):
				self._buy = 'BUY'
		return self._buy
	def cal_sell(self, myindex):
		self._sell = '\t'
		if((mystartindex - myindex) < 1):
			return self._sell
		else:
			if(self._truevalue > float(mysell[1:])):
				self._sell = 'SELL'
		return self._sell


class MP:
	def cal_indicator(self, myindex):
		if  ((mystartindex - myindex) < (my_cal_length-1)):
			return ''
		elif ((mystartindex - myindex) >= (my_cal_length-1)):
			temp = 0
			prev_temp = 0
			for i in range(myindex+9, (myindex - 1), -1):
				temp += float(mydict['Time Series (Daily)'][mydatelist[i]]['4. close'])
				prev_temp += float(mydict['Time Series (Daily)'][mydatelist[i+1]]['4. close'])
			self._indicator = temp / my_cal_length
			self._indicator_prev = prev_temp / my_cal_length
		return '%.4f'%self._indicator	
	def cal_buy(self, myindex):
		self._buy = '\t'
		if  ((mystartindex - myindex) < (my_cal_length-1)):
			return self._buy
		elif ((mystartindex - myindex) >= (my_cal_length-1)):
			self._today_close = float(mydict['Time Series (Daily)'][mydatelist[myindex]]['4. close'])
			self._yesterday_close = float(mydict['Time Series (Daily)'][mydatelist[myindex+1]]['4. close'])
			if((self._today_close > self._indicator) and (self._yesterday_close < self._indicator_prev)):
				self._buy = 'BUY'
		return self._buy
	def cal_sell(self, myindex):
		self._sell = '\t'
		if  ((mystartindex - myindex) < (my_cal_length-1)):
			return self._sell
		elif ((mystartindex - myindex) >= (my_cal_length-1)):
			self._today_close = float(mydict['Time Series (Daily)'][mydatelist[myindex]]['4. close'])
			self._yesterday_close = float(mydict['Time Series (Daily)'][mydatelist[myindex+1]]['4. close'])
			if((self._today_close < self._indicator) and (self._yesterday_close > self._indicator_prev)):
				self._sell = 'SELL'
		return self._sell

		

class MV:
	def cal_indicator(self, myindex):
		if  ((mystartindex - myindex) < (my_cal_length-1)):
			return ''
		elif ((mystartindex - myindex) >= (my_cal_length-1)):
			temp = 0
			prev_temp = 0
			for i in range(myindex+9, (myindex - 1), -1):
				temp += float(mydict['Time Series (Daily)'][mydatelist[i]]['5. volume'])
				prev_temp += float(mydict['Time Series (Daily)'][mydatelist[i+1]]['5. volume'])
			self._indicator = temp / my_cal_length
			self._indicator_prev = prev_temp / my_cal_length
		return '%d'%self._indicator	
	def cal_buy(self, myindex):
		self._buy = '\t'
		if  ((mystartindex - myindex) < (my_cal_length-1)):
			return self._buy
		elif ((mystartindex - myindex) >= (my_cal_length-1)):
			self._today_close = float(mydict['Time Series (Daily)'][mydatelist[myindex]]['5. volume'])
			self._yesterday_close = float(mydict['Time Series (Daily)'][mydatelist[myindex+1]]['5. volume'])
			if((self._today_close > self._indicator) and (self._yesterday_close < self._indicator_prev)):
				self._buy = 'BUY'
		return self._buy
	def cal_sell(self, myindex):
		self._sell = '\t'
		if  ((mystartindex - myindex) < (my_cal_length-1)):
			return self._sell
		elif ((mystartindex - myindex) >= (my_cal_length-1)):
			self._today_close = float(mydict['Time Series (Daily)'][mydatelist[myindex]]['5. volume'])
			self._yesterday_close = float(mydict['Time Series (Daily)'][mydatelist[myindex+1]]['5. volume'])
			if((self._today_close < self._indicator) and (self._yesterday_close > self._indicator_prev)):
				self._sell = 'SELL'
		return self._sell


class DP:
	def cal_indicator(self, myindex):
		if  ((mystartindex - myindex) < (my_cal_length-1)):
			self._indicator = ''
		elif ((mystartindex - myindex) >= (my_cal_length-1)):
			temp = 0
			for i in range(myindex+9, (myindex - 1), -1):
				if ((float(mydict['Time Series (Daily)'][mydatelist[i]]['4. close']) - float(mydict['Time Series (Daily)'][mydatelist[i+1]]['4. close'])) > 0 ):
					temp += 1
				elif ((float(mydict['Time Series (Daily)'][mydatelist[i]]['4. close']) - float(mydict['Time Series (Daily)'][mydatelist[i+1]]['4. close'])) < 0):
					temp -= 1
			self._indicator = temp
		return self._indicator			
	def cal_buy(self, myindex):
		self._buy = '\t'
		if  ((mystartindex - myindex) < (my_cal_length-1)):
			return self._buy
		if self._indicator > int(mybuy):
			self._buy = 'BUY'
		return self._buy
	def cal_sell(self, myindex):
		self._sell = '\t'
		if  ((mystartindex - myindex) < (my_cal_length-1)):
			return self._sell
		if self._indicator < int(mysell):
			self._sell = 'SELL'
		return self._sell

class DV:
	def cal_indicator(self, myindex):
		if  ((mystartindex - myindex) < (my_cal_length-1)):
			self._indicator = ''
		elif ((mystartindex - myindex) >= (my_cal_length-1)):
			temp = 0
			for i in range(myindex+9, (myindex - 1), -1):
				if ((float(mydict['Time Series (Daily)'][mydatelist[i]]['5. volume']) - float(mydict['Time Series (Daily)'][mydatelist[i+1]]['5. volume'])) > 0 ):
					temp += 1
				elif ((float(mydict['Time Series (Daily)'][mydatelist[i]]['5. volume']) - float(mydict['Time Series (Daily)'][mydatelist[i+1]]['5. volume'])) < 0):
					temp -= 1
			self._indicator = temp
		return self._indicator			
	def cal_buy(self, myindex):
		self._buy = '\t'
		if  ((mystartindex - myindex) < (my_cal_length-1)):
			return self._buy
		if self._indicator > int(mybuy):
			self._buy = 'BUY'
		return self._buy
	def cal_sell(self, myindex):
		self._sell = '\t'
		if  ((mystartindex - myindex) < (my_cal_length-1)):
			return self._sell
		if self._indicator < int(mysell):
			self._sell = 'SELL'
		return self._sell


if __name__ == '__main__':
	api_key = pulling_api_key("./api_key.txt")
	mysymbol = input('input your symbol     ')
	mystartdate = input('start date, YYYY-MM-DD ')
	myenddate = input('end date, YYYY-MM-DD ')
	mycommand = input('input your command ')
	mycommand_list = mycommand.split(' ')


	if mycommand.startswith('TR'):
		myoption = mycommand_list[0]
		mybuy = mycommand_list[1]
		mysell = mycommand_list[2]
	else:
		myoption = mycommand_list[0]
		my_cal_length = int(mycommand_list[1])
		mybuy = mycommand_list[2]
		mysell = mycommand_list[3]
	
	mydict = pull_web_n_store_into_dict(mysymbol, api_key)
	mydatelist = create_hash_keys_of_dates_for_cal(mydict)

	mystartindex, myendindex, mydatelength = find_the_length_of_dates(mystartdate, myenddate)
	

	result_outcome(myoption)

	
	

	
	
	