import connect_mysql

def read_temperature():
	file = open ('../files/temperature.txt','r')
	lines = file.readlines()
	print "I have read"
	for data in lines:
		words = data.split(',')
		#measurement fields: node_id,date,mea,type_mea
		connect_mysql.insert_meas(words[0],words[1],words[3],words[4])
	print "I have inserted all, about to close the file"
	file.close()
	
print "I'm in connection"
connect_mysql.init_db()

print "I'm starting temp"
read_temperature()

print "I'm about to close"
connect_mysql.db_close()
