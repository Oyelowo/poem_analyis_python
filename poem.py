# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:20:22 2018

@author: oyeda
"""

#Getting the document directly online
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import pylint
import io
import sys

#READING DIRECTLY FROM THE HTML PAGE
file = urllib.request.urlopen("http://runeberg.org/kalevala/42.html")
document= bs(file.read()).get_text()
start=document.find('Kahdesviidettä runo')
end=document.find('Project Runeberg,')
poem=document[start:end]


#READING FROM THE USER DIRECTORY
poem_filepath = "C:/Users/oyeda/Desktop/Oyedayo_Oyelowo_verto_data_analyst/poem.txt"
poem_open=open(poem_filepath)
poem=poem_open.read()
print(poem)

# =============================================================================
# import os
# print(os.getcwd())
# 
# 
# import os
# dir = os.path.dirname(__file__)
# filename = os.path.join(dir, 'poem.txt')
# filename
# #file:///C:/Users/oyeda/Desktop/Oyedayo_Oyelowo_verto_data_analyst/python_script
# import os
# import sys,os
# sys.path.append(os.path.realpath("Oyedayo_Oyelowo_verto_data_analyst/poem.txt"))
# 
# import csv
# import os.path
# 
# my_path = os.path.abspath(os.path.dirname(__file__))
# path = os.path.join("Oyedayo_Oyelowo_verto_data_analyst/poem.txt")
# with open(path) as f:
#     test = [line for line in csv.reader(f)]
# 
# os.getcwd()
# os.chdir('C:/Users/oyeda/Desktop/Oyedayo_Oyelowo_verto_data_analyst/')
# print(os.listdir())
# 
# 
# print(os.environ.get('HOME'))
# os.path.dirname("Oyedayo_Oyelowo_verto_data_analyst/poem.txt")
# os.path.exists("Oyedayo_Oyelowo_verto_data_analyst/poem.txt")
# os.path.isdir("Oyedayo_Oyelowo_verto_data_analyst/poem.txt")
# os.path.isfile("Oyedayo_Oyelowo_verto_data_analyst/poem.txt")
# os.path.splitext("Oyedayo_Oyelowo_verto_data_analyst/poem.txt")
# 
# from pathlib import Path
# 
# data_folder = Path("Desktop/Oyedayo_Oyelowo_verto_data_analyst/")
# 
# file_to_open = data_folder / "poem.txt"
# 
# f = open(file_to_open)
# 
# print(f.read())
# 
# 
# # Set the directory you want to start from
# rootDir = '.poem.txt'
# for dirName, subdirList, fileList in os.walk(rootDir):
#     print('Found directory: %s' % dirName)
#     for fname in fileList:
#         print('\t%s' % fname)
# =============================================================================





os.path.abspath("poem.txt")
jj=os.path.abspath("poem.txt")
kkn=(open(jj).read())




for key in kl.keys():
     print("dictionary includes", key)

for key, value in kl.items():
      print(key, "=", value)
     
#I chose not to use dictionaries because, it does not allow repetition of elements.
#I did not use set either, because it is unordered.
#Although, it is also possible to use "defaultdict(list)" which can help a
#dictionary to take a list, I chose to use an approach I feel is more optimal.
      
      
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
    print(i+1)
    sf.loc[i+1,'words']= ele
    count= poem_body_lowercase.count(ele)
    sf.loc[i+1,'counts']= count
    sf.loc[i+1, 'time']= i+1
    rt=[i for i, val in enumerate(poem_body_lowercase) if val==ele]
    if len(rt)>1:
        k=[]
        for ind in range(len(rt)):
            if ind+1 <len(rt):
                t1, t2=rt[ind], rt[ind+1]
                delta_t=t2-t1
                k.append(delta_t)
                ind+=1
            av=np.mean(k)
            sf.loc[i+1, 'avg_wt']=av
    else:
        sf.loc[i+1, 'avg_wt']=0

v=sf.groupby(by='words', sort=True)

b=pd.DataFrame()
b['word']=None
for key, group in v:
    for i,r in group.iterrows():
        b.loc[key,'word']=key
        b.loc[key,'count']= r.counts
        b.loc[key, 'avg_wt']=r.avg_wt
b=b.sort_values(by='count', ascending=False)
b=b.reset_index(drop=True)
b=b[0:100]
    

import distance
sent1 = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
sent2 = ['the', 'lazy', 'fox', 'jumps', 'over', 'the', 'crazy', 'dog']
distance.levenshtein(sent1, sent2)
    
distance.levenshtein("lenvestein", "levenshtein")
distance.levenshtein("lowo", "lowo")
distance.levenshtein(sent1, sent2)
        
distance.hamming("hamming", "hamning")
distance.hamming("lowo", "lowo")


distance.levenshtein("decide", "resize", normalized=True)
distance.hamming("decide", "resize", normalized=True)

distance.sorensen("decide", "resize")
distance.jaccard("decide", "resize")


>>> distance.hamming("fat", "cat", normalized=True)
0.3333333333333333
>>> distance.nlevenshtein("abc", "acd", method=1)  # shortest alignment
0.6666666666666666
>>> distance.nlevenshtein("abc", "acd", method=2)  # longest alignment
0.5
