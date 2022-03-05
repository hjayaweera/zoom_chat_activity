# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 13:06:24 2022

@author: hiran
"""
import pandas as pd
import numpy as np


fn1="meeting_saved_chat.txt"

a=np.array([])
f = open(fn1, "r")
i=0
for x in f:
    if x[17:17+3]=="sea": 
        print(i,"  ",x[15:15+8]) 
        a=np.append(a,x[15:15+8])
        i=i+1
    
f.close() 

print(a)

from collections import Counter
letter_counts = Counter(a)
df = pd.DataFrame.from_dict(letter_counts, orient='index')
df=df.sort_values(0,ascending=False)
df.plot(kind='bar')