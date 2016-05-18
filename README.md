# Fault-Detection-in-Networks
Reaction module to errors on Layer 1 and Layer 2 of the OSI Networking Model and generating smart notifications for the same.

1.)The First module which works on Layer-1 deals with "Packet Drops Due to Input Errors" . Two python scripts run to fetch data and react based on it.

owndb.txt: OBSERVIUM fetches "ifInErrors" from the switches using SNMP, we in-turn fetch relevant data from the observium db into another local db called company2.

layer_1_reaction.py :  Pushes config changes to the switches using EAPI using the data fetched from "company2" db.

2.)The second module works on Layer-2 and deals with "Uneven Load balancing in a Port-channel"

eapi-fetch_port_channel.py: Fetches link utilization for the links in a port-channel to a local database called "port_c".

port_channel_reaction.py: Reacts to the fault based on the inputs from the database "port_c" and generates alearts.
