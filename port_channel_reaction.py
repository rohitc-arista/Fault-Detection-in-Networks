import MySQLdb as mdb

connection = mdb.connect (host = "localhost",
                              user = "root",
                              passwd = "snmp",
                              db = "port_c")
with connection:
	cursor1 = connection.cursor(mdb.cursors.DictCursor)
	
	cursor1.execute("SELECT * from port_channel")

	rows1 = cursor1.fetchall()
	sum=0
	sm=0
	sr=11111111
	arr=[]
	arr1=[]

	avv=20
	for row in rows1:
		var=row['poc_desc']
		if sr!=var:
			for aq in rows1:
				if aq['poc_desc']==var:
					sr=var
					arr.append(aq['po_desc'])
					arr1.append(aq['rate'])
			ma=max(arr1)
			mi=min(arr1)
			d=ma-mi
			#print d
			if d>=10:
			   for s in arr1:
				sum=sum+s
				
			   l=len(arr1)
		       	   sum=float(sum)
			   l=float(l)
			   av=sum/l
			 #  print av
				
			   for a in arr1:
				if a>avv:
				#    print a 
				    sm=sm+1
			    
				
		     	   sm=float(sm)
			  # print sm
		
			   perc=(sm/l)*100
			   #print perc

			   #print str(arr)			

                       	   if perc<50:
				print 'problem in '+str(var)+' '
				#! /usr/local/bin/python


				SMTPserver = 'smtp.att.yahoo.com'
				sender =     'netadmi1231@yahoo.com'
				destination = ['netadmi1231@yahoo.com']
				USERNAME = "netadmi1231@yahoo.com"
				PASSWORD = "11061026123"

				# typical values for text_subtype are plain, html, xml
				text_subtype = 'plain'
				
				content="Port channel: "+str(var)+"is unbalanced. Interface:"+str(arr)+"have rates"+str(arr1)+"respectively"

				subject="Sent from PythonScript"

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


	




					
				
