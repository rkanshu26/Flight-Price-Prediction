# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 13:11:25 2020

@author: rk
"""
import requests

url = 'http://127.0.0.1:5000/predict'
r = requests.post(url,json={'Airline':0, 'Source':9, 'Destination':6,
                            'Total Stops': 2, 'Month':2,'Date':4,'Duration_Hour':4,
                            'Duration_Minute':33,'Arrival_Hour':4,'Arrival_Minute':35,
                           'Departure_Hour':2,'Departure_Minute':33,'Additional_Info':8,'Route_1':3,
                           'ROute_2':33,'Route_3':22,'Route_4':12,'Route_5':34})

print(r)