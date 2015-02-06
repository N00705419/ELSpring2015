#!/usr/bin/python
""" Franz Vezuli
	Embedded Linux
	Temperator	Script	"""

import os
import time

"""Need this to write to CSV File"""
import csv 

""" Log Current Time, Temperature in Celsius and Fahrenheit
 Returns a list [time, tempC, tempF] """
 
 
def readTemp():
	tempfile = open("/sys/bus/w1/devices/28-0000069816ee/w1_slave")
	tempfile_text = tempfile.read()
	currentDate=time.strftime('%x')
	currentTime=time.strftime('%x')
	tempfile.close()
	tempC=float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF=tempC*9.0/5.0+32.0
	
	"""Write out to a CSV file, but first make sure it writes only to the last line"""
	
	with open('data.csv', 'wb') as f:
		f.seek(0, os.SEEK_END)
		writer = csv.writer(f, delimiter=',', lineterminator='\n')
		data = [currentDate, currentTime, tempC, tempF]
		writer.writerow(data)
		
	return [currentDate, currentTime, tempC, tempF]

	
print readTemp()