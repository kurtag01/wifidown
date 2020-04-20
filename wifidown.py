#!/usr/bin/python3

location = "/etc/config/wireless"
connect = False
dns = False
there = False

#Set the wifi correctly:
with open (location, "r") as file:
    wifi = file.readlines()
    for line in wifi:
        if 'wwan' in line:
            connect = True            
        if '209.222.18.218 209.222.18.222' in line:
            dns = True
        if "'option disabled '1'" in line:
            there = True
                      
if connect == True and there == False:
    with open(location, "a") as file:
        file.writelines("\toption disabled '1'")
      
if dns == False:
    with open(location, "a") as file:
        file.writelines("\n\toption dns '209.222.18.218 209.222.18.222'")    
