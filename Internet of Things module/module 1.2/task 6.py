from sense_hat import SenseHat
import time
import datetime
import sys

sense = SenseHat()
sense.clear()
starttime = time.time()
i = 0

dataFile = open('record.txt', 'w')

while i <= 50:
	
	time.sleep(1 - ((time.time() - starttime) % 1))
	temp = sense.get_temperature()
	temp = round(temp, 2)

	datetime_object = datetime.datetime.now()
	
	print datetime_object, temp
	dataFile.write(str(datetime_object)+'\t')
	dataFile.write(str(temp)+'\n')
	i = i + 1



