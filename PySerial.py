import time
import serial
import urllib2
import json


url = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"


ser = serial.Serial('COM3', 9600)

while True:
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    ser.write(str("1" + data[0]["symbol"] + "=" + "$" + data[0]["price_usd"]+" "))
