import pyeapi
import json
import MySQLdb
import time
import sys
v8=0
while 1:
	switches=['mt701']
	shspan={}
	

	v5=0
	v6=0
	

	for x in switches:
	   node = pyeapi.connect_to(x)
	   shspan[x] = node.enable('show port-channel traffic | json',encoding='json')
	   name=node.config('show hostname| json')
	   v2=name[0]['hostname']
	   db = MySQLdb.connect("localhost","root","snmp","port_c" )
	   cursor = db.cursor()		# prepare a cursor object using cursor() method
	   #print showversion[x]
	for x in switches:
	   	data2=shspan[x]
	     	#json output in variable
		d2=data2[0]['result']['portChannels']
	     	#print d
		
	for y1 in d2:
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
				sum=data2[0]['result']['portChannels'][y1]['interfaceTraffic'][key]['inUcastPkts']+data2[0]['result']['portChannels'][y1]['interfaceTraffic'][key]['inMulticastPkts']+data2[0]['result']['portChannels'][y1]['interfaceTraffic'][key]['inBroadcastPkts']
				avg=float(sum/3)
					
				loggit = "INSERT INTO port_channel (sr_no,host_desc,poc_desc,po_desc,inUniPkt,inOctets,rate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
				str=cursor.execute(loggit, (v8,v2,v3,v4,v5,v6,avg))							
				#print str
				print sum					
				print avg
				db.commit()
				break
				
				

		
	db.close()
	num=0
	for remaining in range(10, 0, -1):
	    sys.stdout.write("\r")
	    sys.stdout.write("{:2d} seconds remaining before next fetch.".format(remaining)) 
	    sys.stdout.flush()
	    time.sleep(1)
	    #sys.stdout.write("\rComplete!            \n")
	
		


