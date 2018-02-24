# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 06:48:04 2018

@author: oyeda
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:55:36 2018

@author: oyeda
"""


#Getting the document directly online
import urllib.request
from bs4 import BeautifulSoup as bs
#import pandas as pd
#import numpy as np

#READING DIRECTLY FROM THE HTML PAGE
FILE = urllib.request.urlopen("http://runeberg.org/kalevala/42.html")
DOCUMENT = bs(FILE.read()).get_text()
START = DOCUMENT.find('Kahdesviidettä runo')
END = DOCUMENT.find('Project Runeberg,')
POEM = DOCUMENT[START:END]


#READING FROM THE USER DIRECTORY
POEM_FILEPATH = "C:/Users/oyeda/Desktop/Oyedayo_Oyelowo_verto_data_analyst/poem.txt"
POEM_OPEN = open(POEM_FILEPATH, 'r')
POEM = POEM_OPEN.read()

#REMOVE THE TITLE
POEM_BODY = POEM.lstrip('Kahdesviidettä runo\n')

#CONVERT THE CONTENT TO LOWERCASE
POEM_BODY_LOWERCASE = POEM_BODY.lower()


#CREATE CORRESPONDING TIME COST FOR EVERY WORD
COST_LIST = []
COST = 1
COST_LIST.append(COST)
for i, paragraph in enumerate(POEM_BODY_LOWERCASE.split("\n\n")):
    for j, line in enumerate(paragraph.split("\n")):
        for h in range(len(line.split())):
            if h < len(line.split())-1:
                COST += 1
                COST_LIST.append(COST)
        if j < len(paragraph.split("\n"))-1: 
            COST += 2
            COST_LIST.append(COST)   
    if i < len(POEM_BODY_LOWERCASE.split("\n\n"))-1:
        COST += 6
        COST_LIST.append(COST)
a=COST_LIST


