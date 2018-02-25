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

#READING DIRECTLY FROM THE HTML PAGE
file = urllib.request.urlopen("http://runeberg.org/kalevala/42.html")
document = bs(file.read()).get_text()
start = document.find('Kahdesviidettä runo')
end = document.find('Project Runeberg,')
poem = document[start:end]


#READING FROM THE USER DIRECTORY
poem_filepath = "C:/Users/oyeda/Desktop/Oyedayo_Oyelowo_verto_data_analyst/poem.txt"
poem_open = open(poem_filepath, 'r')
poem = poem_open.read()
print(poem)
poem_open.close()
#ensure it is the beginning of the text
poem_open.seek(0)
poem_open.readlines()
poem_open.readline(5)

import re
#use regular expression to check for new line.
#here, after the newline, it searches for any character. This is done to 
#separate new lines from new paragraph
len(re.findall('\n.',poem))
regex = re.compile('\n.')
ll = regex.split(poem)        
#NEW Paragraph
poem.split('\n\n')
'sdsd olj'.replace(' ', ':_t, ')
poem2=poem

for i in range(6, len(poem2.split('\n\n'))*6, 6):
    print(i)
    poem2=poem2.replace('\n\n',  str(i) + 'WWWWWWWWWW')
print(poem2)

poem_body=poem.lstrip('Kahdesviidettä runo\n')
poem_body_lowercase=poem_body.lower()

dds=[]
for i, ele in enumerate(poem.split()[2:]):
    dd={ele + str(i+1): 't_' + str(i+1)}
    dds.append(dd)
    
sf=pd.DataFrame()
sf['words']=None
for i, ele in enumerate(poem_body_lowercase):
    print(i+1)
    sf.loc[i+1,'words']= ele



count=0
kl=[]
while count< len(poem_body_lowercase.split()):    
    new_word=poem_body_lowercase.split()
    regex = re.compile('\n.')
    new_line = regex.split(poem_body_lowercase)
    new_chapter=poem_body_lowercase.split('\n\n')
    
    
    for i,x in enumerate(new_chapter):
        for m,n in enumerate(x.splitlines()):
            count=m
            kl.append(count)
          
    
    if new_word:
        count+=1
        kl.append(count)
    elif new_line:
        count+=2
        kl.append(count)
    elif new_chapter:
        count+=6
        kl.append(count)
    
 
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
    



zx=POEM_BODY


import re
j=[]
for t, g in enumerate(zx.split()):
    word_t = "{0}: t_{1}".format(g,t+1)
    print(word_t)
    j.append(word_t)

regex = re.compile('\n.')
lines = regex.split(zx)
kg=[]
for t, g in enumerate(lines):
    lines_t = "{0}: t_{1}".format(g,(t+1)*2)
    print(lines_t)
    kg.append(lines_t)
    
    
for t, g in enumerate(zx.split("\n\n")):
    chp_t = "{0}: t_{1}".format(g,(t+1)*6)
    print(chp_t)
    j.append(word_t)
    
len(zx.split("\n\n"))
print(kg)

 introduce a time-axis, as follows:
 new-word: delta t 1 h
 new-line: delta t 2 h
 new chapter (two newlines): delta t 6 h
 you should end up with something like {word_1: t_1, word_2: t_2, ...} 


sonja=[]
for i in zip(zx.split(), COST_LIST):
    sonja.append(i)
    print(i)
vb= np.array([zx.split(), COST_LIST])

j=[]
for t, g in enumerate(zx.split()):
    word_t = "{0}: t_{1}".format(g,t+1)
    


LIST_DELTA_TIME = ["{0}: t_{1}".format(w, t) for w, t in zip(WORD_LIST, COST_TIME_LIST)]
g=[]

for i, j in enumerate(WORD_LIST):
    h={}
    h[j].append(i)

key = WORD_LIST

d = {}
for key, value in zip(WORD_LIST, COST_TIME_LIST):
    if key not in d:
         d[key] = []
    d[key].append(value)


d = defaultdict(list)
for key, value in zip(WORD_LIST, COST_TIME_LIST):
    d[key].append(value)

fg=pd.DataFrame()
#fg['words']=None
for k, v in d.items():
    if len(v)<2:
        fg.loc[k,'words'], fg.loc[k,'avg_tm']=k, 0
        print(k, 0)
    else:
        fg.loc[k,'words'], fg.loc[k,'avg_tm']=k,np.mean(np.diff(v))
        print(k,np.mean(np.diff(v)))

d = defaultdict(list)
for key, value in zip(WORD_LIST, COST_TIME_LIST):
    d[key].append(np.diff(value))

np.diff(d)

for name, age in d.items(): 
        print(name, age)



d.keys
np.diff(x)

ae=[]
#Create an empty dataframe.
WORDS_DATA = pd.DataFrame()
for i, word_in_list in enumerate(WORD_LIST):
    print("Processing Word....{0}/{1}.".format(i + 1, len(WORD_LIST)))
    WORDS_DATA.loc[i, 'words'] = word_in_list
    WORDS_DATA.loc[i, 'count'] = WORD_LIST.count(word_in_list)
#    get the list of positions where each alphabet occured
    le = [[idx, letter] for letter, idx in zip(WORD_LIST, COST_TIME_LIST) if letter == word_in_list]
    if len(le)==0:
    g= np.mean(np.diff(letter_list))
    ae.append(g)
    
    if len(letter_list) > 1:
        delta_time_list = []
        for value, letter in enumerate(letter_list):
            if value + 1 < len(letter_list):
                time1, time2 = letter_list[value], letter_list[value + 1]
                delta_time = time2 - time1
                delta_time_list.append(delta_time)
            WORDS_DATA.loc[i, 'Average_wt_time'] = np.mean(delta_time_list)
    else:
        WORDS_DATA.loc[i, 'Average_wt_time'] = 0


az = dict(zip(WORD_LIST, COST_TIME_LIST))
az = dict((el, g.append(h)) for el,h in zip(WORD_LIST, COST_TIME_LIST))

aa = {"{0}:{1}".format(w, t) for w, t in zip(WORD_LIST, COST_TIME_LIST)}
aa = {}
aa["fg"] =["dffd", "Fssf"]
aa[WORD_LIST] = COST_TIME_LIST




from collections import defaultdict

data_dict = defaultdict(list)
All you have to do is replace

data_dict[WORD_LIST] = COST_TIME_LIST
with

data_dict[WORD_LIST].append(COST_TIME_LIST)

#import distance
#sent1 = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
#sent2 = ['the', 'lazy', 'fox', 'jumps', 'over', 'the', 'crazy', 'dog']
#distance.levenshtein(sent1, sent2)
#    
#distance.levenshtein("lenvestein", "levenshtein")
#distance.levenshtein("logsaf", "jfwo")
#distance.levenshtein(sent1, sent2)
#        
#distance.hamming("hamming", "hamning")
#distance.hamming("aflw", "loaf")
#
#
#distance.levenshtein("decide", "resize", normalized=True)
#distance.hamming("decide", "resize", normalized=True)
#
#distance.sorensen("decide", "resize")
#distance.jaccard("decide", "resize")
#
#
#distance.hamming("fat", "cat", normalized=True)
#0.3333333333333333
#>>> distance.nlevenshtein("abc", "acd", method=1)  # shortest alignment
#0.6666666666666666
#>>> distance.nlevenshtein("abc", "acd", method=2)  # longest alignment
#0.5
