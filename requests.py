# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 10:13:27 2020

@author: rk
"""


import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Airline':2, 'Source':9, 'Destination':6,
                            'Total Stops': 2, 'Month':2,'Date':4,'Duration_Hour':4,
                            'Duration_Minute':33})

print(r.json())