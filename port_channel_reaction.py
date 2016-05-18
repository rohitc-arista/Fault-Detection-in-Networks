import MySQLdb as mdb

connection = mdb.connect (host = "localhost",		
                              user = "root",
                              passwd = "snmp",
                              db = "port_c")			#Connecting to MySql database "port_c"
with connection:
	cursor1 = connection.cursor(mdb.cursors.DictCursor)	#Cursor Object
	
	cursor1.execute("SELECT * from port_channel")		#Fetching records from "port_channel" table

	rows1 = cursor1.fetchall()				#Storing records in a variable
	sum=0
	sm=0
	sr=11111111
	arr=[]
	arr1=[]

	avv=20
	for row in rows1:					#Iterating in the records of "port_channel" table 
		var=row['poc_desc']
		if sr!=var:					#Flag to break loop if port_channel ID matches 
			for aq in rows1:
				if aq['poc_desc']==var:
					sr=var
					arr.append(aq['po_desc'])   #portchannel ID/Description is stored in an array
					arr1.append(aq['rate'])	   #rate of link utilization of the link in port channel
			ma=max(arr1)  					#Maximum Link utilization in the port channel
			mi=min(arr1)					#Minimum Link Utilization in port channel
			d=ma-mi						#Max-Min is calculated
			#print d
			if d>=10:					#If (Max-Min) > 10 we get proceed further inside loop
			   for s in arr1:
				sum=sum+s				#Sum of all link utilization	
				
			   l=len(arr1)
		       	   sum=float(sum)
			   l=float(l)
			   av=sum/l					#Average of all link utilization
			 #  print av
				
			   for a in arr1:			
				if a>avv:				#Number of links whose link utilization greater than average link utilization
				#    print a 
				    sm=sm+1
			    
				
		     	   sm=float(sm)
			  # print sm
		
			   perc=(sm/l)*100  				#percentage of link utiliuzation
			   #print perc

			   #print str(arr)			

                       	   if perc<50:
				print 'problem in '+str(var)+' '		#! /usr/local/bin/python

				SMTPserver = 'smtp.att.yahoo.com'
				sender =     'netadmi1231@yahoo.com'
				destination = ['netadmi1231@yahoo.com']
				USERNAME = "netadmi1231@yahoo.com"
				PASSWORD = "11061026123"

				text_subtype = 'plain'				# typical values for text_subtype are plain, html, xml
				
				content="Port channel: "+str(var)+"is unbalanced. Interface:"+str(arr)+"have rates"+str(arr1)+"respectively"

				subject="Sent from PythonScript"

				import sys
				import os
				import re
				
				from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
				                			   # use this for standard SMTP protocol   (port 25, no encryption)
									   # from smtplib import SMTP
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
				    finally:
					conn.quit()

				except Exception, exc:
				    sys.exit( "mail failed; %s" % str(exc) ) # give a error message



			else:
				print 'no problem in '+str(var)+' '  #Second Check-Using logic

			   arr[:]=[]
			   arr1[:]=[]
	
			else:
				print 'No problem in '+str(var)+' ' #initial check of (Max-Min) Rate 

			arr[:]=[]
			arr1[:]=[]


	




					
				
