import MySQLdb as mdb
import pyeapi

node=pyeapi.connect_to('mt701')		#Connecting to switch mt701


connection = mdb.connect (host = "localhost",		#Connecting to mysql database "company2"
                              user = "root",
                              passwd = "snmp",
                              db = "company2")


arr=[]

with connection:
	cursor1 = connection.cursor(mdb.cursors.DictCursor)		#Making a Cursor Object
					
	cursor1.execute("SELECT * from portst")				#Executing MySql command

	rows1 = cursor1.fetchall()					#Storing fetched rows in a variable

	cursor1.execute("select * from port2")				#Executing MySql command

	rows2 = cursor1.fetchall()					#Storing fetched rows in a variable

	inputerr=[];

	for row in rows1:						#Iterating in the rows of "port_st" table and matching "ifInErrors" value with a threshold value of 50
        	if row["ifInErrors"]>50:
			inputerr.append(row["ifInErrors"])		
			pid= row["port_id"]				#Fetching port-id fot the port which shoes ifInputErrors>50
			#print pid
			for row in rows2:				#Iterating in the rows of "port2" table to get the discription of the port with "ifInErrors">50
				if row["port_id"]==pid:	
					arr.append(row['ifDescr'])
					print "\nInterface shut: %s." %row["ifDescr"] 		
					node.config(['interface'+' '+row["ifDescr"], 'shutdown'])	#Shutting the port
					node.config(['send log message interface '+row["ifDescr"]+' is now shut due to high input errors'])		#Logging a message on the switch
					break
				

	#! /usr/local/bin/python


        SMTPserver = 'smtp.att.yahoo.com'		#Configuration to connect to a Mail server
	sender =     'netadmi1231@yahoo.com'
	destination = ['netadmi1231@yahoo.com']
	USERNAME = "netadmi1231@yahoo.com"
	PASSWORD = "11061026123"

	text_subtype = 'plain'				# typical values for text_subtype are plain, html, xml
				
	content="Interfaces :"+str(arr)+"has been shut down since it has input error of"+str(inputerr)+"  Respectively"		#Content of the email

	subject="Sent from Python"		#SUbject of the mail

	import sys
	import os
	import re
				
	from smtplib import SMTP_SSL as SMTP    	# this invokes the secure SMTP protocol 
							# from smtplib import SMTP                  
							# use this for standard SMTP protocol   
							# old version
							# from email.MIMEText import MIMEText
	from email.mime.text import MIMEText

	try:						#Try Block
		msg = MIMEText(content, text_subtype)
		msg['Subject']=       subject
        	msg['From']   = sender 			# some SMTP servers will do this automatically, not all

		conn = SMTP(SMTPserver)			#Connecting to the server using SMTP
		conn.set_debuglevel(False)		
		conn.login(USERNAME, PASSWORD)		#Authenticating
		try:
			conn.sendmail(sender, destination, msg.as_string())		#Sending Mail
			print "Mail sent to Network Administrator!"
 		finally:
			conn.quit()			#Connectiong CLosed

	except Exception, exc:	
		 sys.exit( "mail failed; %s" % str(exc) ) # give a error message	

	
	

		
	



connection.commit() 

connection.close()

