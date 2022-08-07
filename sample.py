from yahoo_fin import stock_info as si
import datetime
import time
import mysql.connector
import configparser
import os

config = configparser.ConfigParser()
config.read(os.curdir+"/config.txt")
ppwd = config.get("configuration", "password")
    
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd= ppwd,
  database="pricing"
)

def getprice():

    liveprice = si.get_live_price("JPY=X")

    return liveprice
       
def insertdb():

    mycursor = mydb.cursor()
    sql = "INSERT INTO fx (DT, PX) VALUES (%s, %s)"
    val = (datetime.datetime.now().strftime('%Y-%m/%d %H:%M:%S'), float(getprice()))
    mycursor.execute(sql, val)

    mydb.commit()

    print(f"Record {datetime.datetime.now().strftime('%Y-%m/%d %H:%M:%S')} - {round(getprice(),4)}")




while True:
    time.sleep(1)
    insertdb()
    
