import mysql.connector 
from datetime import datetime	

DB_USER = "root"
PASSWORD = "edison123"
DB_NAME = "edison"
DB_SERVER = "10.170.32.17"

#init database connection
def init_db():
	try:
		print ":D"
		#create connection
		cnx = mysql.connector.connect(user 	= DB_USER, 
					      password 	= PASSWORD,
                        	      	      host 	= DB_SERVER,
                                	      database 	= DB_NAME)
		print "D:"

	except mysql.connector.Error as err:
		print "Failed to connect"
		print err
	
	#create the cursor
	cursor = cnx.cursor()

#insert alerts
def insert_alerts(id,date,node_id):

	add_alerts = ("INSERT INTO alerts "
	           "(date, node_id)"
	           "VALUES (%s, %d)")

	data_alerts = (today,node_id)
	#insert data function usage
	insert_data(add_alerts, data_alerts)

#insert measurements
def insert_meas(node_id,date,mea,type_mea):
	add_meas = ("INSERT INTO meas "
		    "(node_id,date,mea,type_mea)"
		    "VALUES (%(node_id)s,%(date)s,%(mea)s,%(type_mea)s)")
	data_meas = {
		   'node_id'	: node_id,
		   'date'	: date,
		   'mea'	: mea,
		   'type_mea'	: type_mea,
	}
	#insert data function usage
	insert_data(add_meas, data_meas)

#insert measurements type
def insert_meas_type (id, type, unit):
	add_meas_type = ("INSERT INTO meas_type "
		         "(id, type, unit)"
		         "VALUES (%(id)s,%(type)s,%(unit)s)")
	data_meas_type = {
		         'id' 	: id, 
		         'type'	: type,
		         'unit'	: unit,
	}
	#insert data function usage
	insert_data(add_meas_type, data_meas_type)
	
#insert nodes
def insert_nodes(latitud, longitud):

	add_nodes = ("INSERT INTO nodes "
	  	     "(latitud, longitud)"
	   	     "VALUES (%(latitud)s, %(longitud)s)")
	data_nodes = {
		    'latitud' : latitud,
		    'longitud' : longitud,
	}
	#insert data function usage
	insert_data(add_nodes, data_nodes)


#insert data function
def insert_data(type, value):
	try:
		#try to execute
		cursor.execute(type,value)
		# Make sure data is committed to the database
		cnx.commit()
	except Exception as e:
		print "Failed to insert data"
		print e

'''
#query from alerts
def query_alerts():

	query = ("SELECT id, state, node_id FROM alerts ")
	try:
		cursor.execute(query)
		for (id, state,node_id) in cursor:
    			print ("id {}, state {}, node_id{}".format(
        		id, state, node_id))

	except Exception as e:
		print "Failed to retrieve data"
		print e

#query from measurements
def query_measurements():

	query = ("SELECT node_id, date, mea, type_mea FROM meas ")
	try:
		cursor.execute(query)
		for (node_id, date, mea, type_mea) in cursor:
    			print ("node_id {}, date {}, mea{}, 
			type_mea".format(id, state, node_id))

	except Exception as e:
		print "Failed to retrieve data"
		print e

#query from measurements types
def query_measurements_types():

	query = ("SELECT id, type, unit FROM meas_type ")
	try:
		cursor.execute(query)
		for (id, type, unit) in cursor:
    			print ("id {}, type {}, unit{}".format(
        		id, type, unit))

	except Exception as e:
		print "Failed to retrieve data"
		print e
	
#query from nodes
def query_nodes():
	
	query = ("SELECT latitud, longitud FROM nodes ")
	try:
		cursor.execute(query)
		for (latitud, longitud) in cursor:
    			print ("latitud {}, longitud {}".format(
        		latitud, longitud))

	except Exception as e:
		print "Failed to retrieve data"
		print e
'''

#end of session
def db_close():
	#End of the program
	cursor.close()
	cnx.close()
