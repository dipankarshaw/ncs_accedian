import time
import json
import os
import sys
import yaml
import re
from pprint import pprint
from netmiko import Netmiko
import datetime
from jinja2 import Template
import csv
import textfsm
from service import Service
import yaml
#from Class_Based_Spirent_Code_Generation import Spirent_L2_Traffic_Gen,Get_Spirent_Config,Create_Spirent_L2_Gen

dict1 = yaml.load(open('templates/inputfile_ACCA.yml'),Loader=yaml.Loader)
my_config = Service(**dict1)
meg_index = my_config.parse_accedian()
#print(json.dumps(dict1,indent=4))
my_config = Service(**dict1)
my_config.Command_Creation()
#my_config.push_config()
#my_config.delete_config()
#my_config.Validate_ccm()
my_config.Y1564_test()


# Spirent_L2_Gen = Create_Spirent_L2_Gen()
# Spirent_L2_Gen.Port_Init()
# print("Just Before Stream Creation-1")
# StreamHandle = Spirent_L2_Gen.Stream_Config_Creation_Without_VLAN_Mbps(0,1)
# #Spirent_L2_Gen.Generate_Stream_Traffic(StreamHandle)
# print("Just Before Stream Creation-2")
# StreamHandle = Spirent_L2_Gen.Stream_Config_Creation_Without_VLAN_Mbps(1,0)
# #Spirent_L2_Gen.Generate_Stream_Traffic(StreamHandle)
# Spirent_L2_Gen.Generate_Traffic()
# Spirent_L2_Gen.Traffic_Collection()
# Status = Spirent_L2_Gen.Validate_Traffic_Result()

#Spirent_InputParam = {'Ether_Speed':'ether1000', 'Stream_Name':'Spirent_Class_Test', 'Frame_Size':2000, 'Rate_Mbps': 100}