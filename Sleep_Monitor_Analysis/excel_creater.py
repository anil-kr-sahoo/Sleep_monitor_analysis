# import xlsxwriter module
import xlsxwriter
from datetime import datetime, timedelta
import random

workbook = xlsxwriter.Workbook('sleep_monitor.xlsx')
ws = workbook.add_worksheet("My sheet")
ws.write(0, 0, "Date")
ws.write(0, 1, "Time")
ws.write(0, 2, "Sleep_Pecrcent")

start_date = datetime.now().replace(day=1,month=1,hour=00,minute=00,second=00)
end_date = datetime.now()

total_days = end_date - start_date
row = 1
column = 0
sleep_pecrcent = 0

for days in range(total_days.days+1):
	date_time = start_date + timedelta(days=days)
	choose_randm_hr = random.randint(12,16)	
	for hour in range(0,24):
		present_date_time = date_time.replace(hour=hour)
		hour = present_date_time.hour
		minute = present_date_time.minute
		time = ("%02d" %hour) + ":" + ("%02d" %minute)
		if present_date_time > datetime.now():
			break
		#----------------night sleep
		if hour == 22:
			sleep_pecrcent = random.randint(10, 50)
		elif hour == 23:
			sleep_pecrcent = random.randint(20, 60)
		elif hour == 0:
			sleep_pecrcent = random.randint(30, 70)
		elif hour == 1:
			sleep_pecrcent = random.randint(40, 80)
		elif hour == 2:
			sleep_pecrcent = random.randint(50, 90)
		elif hour == 3:
			sleep_pecrcent = random.randint(60, 100)
		elif hour == 4:
			sleep_pecrcent = random.randint(40, 80)
		elif hour == 5:
			sleep_pecrcent = random.randint(20, 60)
		elif hour == 6:
			sleep_pecrcent = random.randint(10, 50)
		else:
			sleep_pecrcent = 0
		#---------------day nap
		if hour == choose_randm_hr:
			sleep_pecrcent = random.randint(10, 50)
		elif hour == choose_randm_hr+1:
			sleep_pecrcent = random.randint(20, 60)
		elif hour == choose_randm_hr+2:
			sleep_pecrcent = random.randint(10, 50)

		ws.write(row, column, str(date_time.date()))
		ws.write(row, column+1, time)
		ws.write(row, column+2, sleep_pecrcent)
		row += 1
workbook.close()
