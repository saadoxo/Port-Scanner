#!/bin/python3

import sys
import socket
from datetime import datetime

#Defining out target

if len(sys.argv) == 2:
          target  = socket.gethostbyname(sys.argv[1])  #Translates hostname to IPv4

else: 
     print("ERROR! \nInvalid amount of aruguments")
     print("Syntax:./scannner.py <ip>") 
     target = "No Target Found"
     
     
#Adding a pretty banner 
print("-" * 50)
print("Scanning Target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)


try:
       for port in range(50,85):
           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           socket.setdefaulttimeout(1)
           result = s.connect_ex((target,port)) #returns an error indicator - ex
           if result == 0:
                print("Port {} is open".format(port))
           s.close()
                
except KeyboardInterrupt:
        print("\nExiting Progam.")
        sys.exit()

except socket.gaierror:
       print("Host name could not be resolved")
       sys.exit()
       
except socket.error:
       print("Couldn't connect to the server.")
       sys.exit()

















