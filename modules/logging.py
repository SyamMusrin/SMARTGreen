#Logging Function
import pymysql

from settings import *


connection = pymysql.connect(host=rds_host, user=rds_user,
 password=rds_pass, database=rds_db_name)

class Logging():
	#Checks for last entry
	def last():
		# Create a cursor
		cursor = connection.cursor()
		# Execute SELECT query
		query = "SELECT audioname FROM audio_samples WHERE dataset_id = 1 ORDER BY sample_id DESC LIMIT 1"

		cursor.execute(query)
		# Fetch the result
		result = cursor.fetchone()

		# Extract the number
		number = ''.join(filter(str.isdigit, result[0]))

		return number
