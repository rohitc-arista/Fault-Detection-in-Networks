# Fault-Detection-in-Networks

H/W used in the project:

1.Arista Switches running software image version greater than 4.15
2.Any linux running machine to configure as a central server.

S/W Used in the project:

1.VirtualBoxVM : To host the central server.
2.Python 
3.EAPI : For Arista specific solution to faults.
4.SNMP : For a generic solution to the faults.
5.Observium : Observium is an SNMP too whichis used to fetch data to the central server.

*****************************************************************************************************************************
OVERVIEW
This project focuses on identifying faults on Layer-1 and Layer-2 of the OSI networking model and providing resilience and smart notifications to the system admin. Further we are focussing on "Packet drops due to inputErrors" on Layer-1 and 
"Uneven Load balancing in a port-channel" on Layer-2


Reaction module to errors on Layer 1 and Layer 2 of the OSI Networking Model and generating smart notifications for the same:

*****************************************************************************************************************************
MODULE-1
The First module which works on Layer-1 deals with "Packet Drops Due to Input Errors" . Two python scripts run to fetch data and react based on it. The scripts and what they do is given below:

owndb.txt: OBSERVIUM fetches "ifInErrors" from the switches using SNMP, we in-turn fetch relevant data from the observium db            into another local db called company2.

layer_1_reaction.py : Pushes config changes to the switches using EAPI using the data fetched from "company2" db. The reactin                       here is to shut the interface also send a log message and a mail aleart to the Network Admin.

*****************************************************************************************************************************
MODULE-2
2.)The second module works on Layer-2 and deals with "Uneven Load balancing in a Port-channel"

eapi-fetch_port_channel.py: Fetches link utilization for the links in a port-channel to a local database(MySql) called                                   "port_c".

port_channel_reaction.py: Reacts to the fault based on the inputs from the database "port_c" and generates alerts to the                              System Admin in the form of e-mail using SMTP

*****************************************************************************************************************************
