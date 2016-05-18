import MySQLdb as mdb
import pyeapi

node=pyeapi.connect_to('mt701')


connection = mdb.connect (host = "localhost",
                              user = "root",
                              passwd = "snmp",
                              db = "company2")


arr=[]

with connection:
	cursor1 = connection.cursor(mdb.cursors.DictCursor)
	
	cursor1.execute("SELECT * from portst")

	rows1 = cursor1.fetchall()

	cursor1.execute("select * from port2")

	rows2 = cursor1.fetchall()

	inputerr=[];

	for row in rows1:
        	if row["ifInErrors"]>50:
			inputerr.append(row["ifInErrors"])
			pid= row["port_id"]
			#print pid
			for row in rows2:
				if row["port_id"]==pid:	
					arr.append(row['ifDescr'])
					print "\nInterface shut: %s." %row["ifDescr"] 
					node.config(['interface'+' '+row["ifDescr"], 'shutdown'])#code to shut an interface goes here.
					node.config(['send log message interface '+row["ifDescr"]+' is now shut due to high input errors'])
					break
				

	#! /usr/local/bin/python


        SMTPserver = 'smtp.att.yahoo.com'
	sender =     'netadmi1231@yahoo.com'
	destination = ['netadmi1231@yahoo.com']
	USERNAME = "netadmi1231@yahoo.com"
	PASSWORD = "11061026123"

        # typical values for text_subtype are plain, html, xml
	text_subtype = 'plain'
				
	content="Interfaces :"+str(arr)+"has been shut down since it has input error of"+str(inputerr)+"  Respectively"

	subject="Sent from Python"

	import sys
	import os
	import re
				
	from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
	# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

	# old version
	# from email.MIMEText import MIMEText
	from email.mime.text import MIMEText

	try:
		msg = MIMEText(content, text_subtype)
		msg['Subject']=       subject
        	msg['From']   = sender # some SMTP servers will do this automatically, not all

		conn = SMTP(SMTPserver)
		conn.set_debuglevel(False)
		conn.login(USERNAME, PASSWORD)
		try:
			conn.sendmail(sender, destination, msg.as_string())
			print "Mail sent to Network Administrator!"
 		finally:
			conn.quit()

	except Exception, exc:
		 sys.exit( "mail failed; %s" % str(exc) ) # give a error message

	
	

		
	



connection.commit() 

connection.close()

