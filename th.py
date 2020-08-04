from netmiko import ConnectHandler
from multiprocessing import Pool
import os
import json
from time import strftime, localtime
from datetime import datetime
import sys
import csv
import yaml
from pprint import pprint


maxhosts = 5
dict1 = yaml.load(open("templates/inputfile_ACCA.yml"),Loader=yaml.Loader)
devicelist = []
for items in dict1['site_list']:
    devicelist.append(items['login'])
def HitDevice(*devicelist):
    net_connect = ConnectHandler(**devicelist[0])
    with open('templates/XC_command_{}_create.txt'.format(devicelist[0]["host"]),'r') as f:
        f2 = f.readlines()
        output = net_connect.send_config_set(f2)
        if devicelist[0]['device_type'] == 'cisco_xr':
            net_connect.commit()
        print(output)
        net_connect.exit_config_mode()
        net_connect.disconnect()

with Pool(maxhosts) as dipankar:
    dipankar.map(HitDevice,devicelist)