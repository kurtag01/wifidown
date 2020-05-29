#!/usr/bin/python3

import os

location = "/etc/config/wireless"
location2 = "/etc/config/network"

connect = False
dns = False
there = False

#Set the wifi correctly:
with open(location, "r") as file:
    wifi = file.readlines()
    for line in wifi:
        if 'wwan' in line:
            connect = True
        if "option disabled '1'" in line:
            there = True

#check to see if dns has already been written
with open(location2, "r") as file:
    stuff = file.readlines()
    for line in stuff:
        if '208.67.222.222' in line:
            dns = True
            
#now we write the files
if connect == True and there == False:
    with open(location, "a") as file:
        file.writelines("\toption disabled '1'")

if dns == False and connect == True:
    with open(location2, "r+") as old_file, open("/etc/config/network.new", "w") as new_file:
        for line in old_file:
            new_file.write(line)
            if 'dhcp' in line:
                new_file.write("\tlist dns '208.67.222.222'\n\tlist dns '1.1.1.1'\n\toption peerdns '0'\n")

os.rename("/etc/config/network.new", location2)

