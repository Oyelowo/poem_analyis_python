# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:20:22 2018

@author: oyeda
"""

#Getting the document directly online
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd

file = urllib.request.urlopen("http://runeberg.org/kalevala/42.html")
document= bs(file.read()).get_text()
start=document.find('Kahdesviidettä runo')
end=document.find('Project Runeberg,')
poem=document[start:end]
print(poem)


poem_filepath = "C:/Users/oyeda/Desktop/Job_Tasks/poem.csv"
poem= pd.read_csv(poem_filepath)

fg=[]
for i in range(1,101):
    a='word_' + str(i) + ':' +'t_' + str(i)
    fg.append(a)
    

#without printing the title which is two words
for i, ele in enumerate(poem.split()[2:]):
    print(i+1, ele)

kl={}
for i, ele in enumerate(poem.split()[2:]):
    kl[ele]= i + 1
    print(i+1, ele)
kl.items
kl.get


for key in kl.keys():
     print("dictionary includes", key)

for key, value in kl.items():
      print(key, "=", value)
      
      
      
#from collections import defaultdict
#
#data_dict = defaultdict(list)
#
#for i in
#data_dict[regNumber] = details
    
poem_body=poem.split()[2:]
poem_body_lowercase=[word.lower() for word in poem_body]
dds=[]
for i, ele in enumerate(poem.split()[2:]):
    dd={ele + str(i+1): 't_' + str(i+1)}
    dds.append(dd)
    
sf=pd.DataFrame()
sf['words']=None
for i, ele in enumerate(poem_body_lowercase):
    sf.loc[i+1,'words']= ele
    count= poem_body_lowercase.count(ele)
    sf.loc[i+1,'count']= count
    


    data.loc[data['first_name'] == 'Antonio', 'city':'email']
#* output the following for the top 100 words by count in the text:
# word, count, average waiting time between subsequent occurrences of the same word in
#the whole text
# * No need to handle punctuation etc. i.e. "upottajahan." is one word.

#new-word: delta t 1 h
# new-line: delta t 2 h
# new chapter (two newlines): delta t 6 h
# you should end up with something like {word_1: t_1, word_2: t_2, ...} 
