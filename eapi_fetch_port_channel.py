import pyeapi
import json
import MySQLdb
import time
import sys
v8=0		#Variable to input serial number into the db
while 1:
	switches=['mt701']		#Host name of the switch to connect to using EAPI
	shspan={}
	

	v5=0		
	v6=0
	

	for x in switches:
	   node = pyeapi.connect_to(x)		#Connecting to devices in "switches"
	   shspan[x] = node.enable('show port-channel traffic | json',encoding='json') #Fetching JSON output for the links in a port-channel into shspan[]
	   name=node.config('show hostname| json')	#Fetching hostname
	   v2=name[0]['hostname']
	   db = MySQLdb.connect("localhost","root","snmp","port_c" )		#connecting to the mysql database "port_c"
	   cursor = db.cursor()		# prepare a cursor object using cursor() method
	   #print showversion[x]
	for x in switches:
	   	data2=shspan[x]		#json output in variable
		d2=data2[0]['result']['portChannels']
	     	#print d
		
	for y1 in d2:			#Iterating in keys to get to a desired value in the dictionary
		v3=y1
		for key in data2[0]['result']['portChannels'][y1]['interfaceTraffic']:
			v4=key
			v8+=1
			sum=0.0
			avg=0.0
			print key
			for key1 in data2[0]['result']['portChannels'][y1]['interfaceTraffic'][key]:				
				#print '*******'
				#print v8							
				#print data2[0]['result']['portChannels'][y1]['interfaceTraffic'][key][inUcastPkts]
				sum=data2[0]['result']['portChannels'][y1]['interfaceTraffic'][key]['inUcastPkts']+data2[0]['result']['portChannels'][y1]['interfaceTraffic'][key]['inMulticastPkts']+data2[0]['result']['portChannels'][y1]['interfaceTraffic'][key]['inBroadcastPkts']	#Calculating link utilization using, Link Util=(inUnicast+inMulticast+inBroadcast)/3
				avg=float(sum/3)
					
				loggit = "INSERT INTO port_channel (sr_no,host_desc,poc_desc,po_desc,inUniPkt,inOctets,rate) VALUES (%s, %s, %s, %s, %s, %s, %s)" 	#inserting values to the database
				str=cursor.execute(loggit, (v8,v2,v3,v4,v5,v6,avg))		#inserting values to the database					
				#print str
				print sum					
				print avg
				db.commit()		#Commiting changes to the database
				break
				
				

		
	db.close()
	num=0
	for remaining in range(10, 0, -1):			#Loop to show timer for next fetch
	    sys.stdout.write("\r")
	    sys.stdout.write("{:2d} seconds remaining before next fetch.".format(remaining)) 
	    sys.stdout.flush()
	    time.sleep(1)
	    #sys.stdout.write("\rComplete!            \n")
	
		


