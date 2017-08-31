

import urllib2 # this is a good connection
import pymysql
import json
# https://www.a2hosting.com/kb/developer-corner/mysql/connecting-to-mysql-using-python # -- there are three methods to connect to MySQL from Python

response = urllib2.urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=EXR&outputsize=compact&apikey=EC4Q6QUNZ7C45UIQ')
json=response.read()
jsondata=response.cursor()
# data=request.json
print('Data In Cursor')
print json
# print (data)
# symbol = request.json('Symbol')
# print('symbol')
# symbol2 = json.get('Symbol')
# print('symbol2')

# /Users/alejandroromero/GitHub/Projects/Stock_Prediction/stock_price_download.py
# python ./Documents/"Alejandro Romero"/"Business Stock Prediction"/stock_price_download.py
def insertDb():
				myConnection = pymysql.connect( host='localhost', port=8889, user='root', passwd='root', db='stock' ) # this is good
				cursor = myConnection.cursor()
				# doQuery(myConnection)
				# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html. -- this is for how to insert data
				add_stock_values = ("INSERT INTO `stock_price`"  "(`Symbol`, `Last_Refreshed`, `Time_Zone`, `Date`, `open`, `high`, `low`, `close`, `volume`)" "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)") %(request.json('Symbol'), request.json('Last_Refreshed'), request.json('Time_Zone'), request.json('Date'), request.json('open'), request.json('high'), request.json('low'), request.json('close'), request.json('volume'))
				print (add_stock_values)
				# data_stock_value = ('EXR', '2017-08-20', 'US/Eastern', '2017-08-19', '75.7100', '75.9900', '75.1500', '75.8200', '435308'), 
				# ('EXR', '2017-08-19', 'US/Eastern', '2017-08-20', '75.7100', '75.9900', '75.1500', '75.8200', '435308');
				# cur = myConnection.cursor() #pymysql.cursors.DictCursor
				# cur.execute(add_stock_values, data_stock_value)
				# cur.execute("INSERT INTO `stock_price` (`Symbol`, `Last_Refreshed`, `Time_Zone`, `Date`, `open`, `high`, `low`, `close`, `volume`) VALUES ('EXR', '2017-08-22', 'US/Eastern', '2017-08-21', '75.7100', '75.9900', '75.1500', '75.8200', '435308');")
				# result_set = cur.fetchall()
				# for row in result_set:
				#     print "%s, %s, %s" % (row["Symbol"], row["open"], row["close"])
				# try:
					#Execute DML and Commit changes
				cursor.execute(add_stock_values, jsondata)
				db.commit()
				cursor.close()
				# except:
				# 	db.rollback()
				# return dumps(("Ok"), default=json_util.default)





				# myConnection.commit()
				# print("DataInserted")
				# cur.close()

				myConnection.close()






# INSERT INTO `stock_price` (`Symbol`, `Last_Refreshed`, `Time_Zone`, `Date`, `open`, `high`, `low`, `close`, `volume`) VALUES ('EXR', '2017-08-23', 'US/Eastern', '2017-08-22', '75.7100', '75.9900', '75.1500', '75.8200', '435308');