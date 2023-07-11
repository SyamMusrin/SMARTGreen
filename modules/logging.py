#Logging Function
import csv
import os
import mysql.connector

conn = pymysql.connect(host=rds_host, user=rds_user,
 password=rds_pass, database=rds_db_name)

class Logging():
	#Checks for last entry
	def Last():
		with open('logs.csv','r') as file: 
			data = file.readlines() 
			last_row = data[-1].rstrip('\n')
			first_column_data = last_row.split(',')[0] 
			return first_column_data

	#Creates a new .csv file
	def Create():
		with open("logs.csv", mode ="w") as csvfile:
			fieldnames = ["no.", "file_format", "sample_rate", "bit_depth", "duration", "date", "time"]
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()

	#Adds a new line to the .csv file
	def Add(add_data):
		file = open("logs.csv", mode = "a", newline = "")
		writer = csv.writer(file)
		writer.writerows(add_data)
		file.close()	

	#logging function
	def New_Entry(file_format, sr, bd, d, date, time):
		#Creates a new entry if logs.csv exist if not create file and input new entry.
		if os.path.isfile('logs.csv'):
			num = int(Logging.Last()) + 1
			add_data = [[num, file_format, sr, bd, d, date, time]]
			#Create a new entry for the .csv file
			Logging.Add(add_data)
		
		else:
			print("logs.csv does not exist. Creating .csv file now...")
			Logging.Create()

			num = 1
			add_data = [[num, file_format, sr, bd, date, time]]
			Logging.Add(add_data)


