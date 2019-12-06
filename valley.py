# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:33:53 2019

@author: Amey
"""
import random
import matplotlib.pyplot as plt
p=0
v=0
n=10
s=[None]*int(n)
dict1={1:'U',2:'D'}
dict2={'U':1,'D':-1}

i=0
for i in range(0,n):
    s[i]=dict1[random.randint(1,2)]
j=0
count=0
for j in range(0,n):
    count=count+dict2[s[j]]
#count number of valleys
x=0
y=0
if count!=0:
    
    if count>0 :
        for x in range(0,abs(count)):
            s.append('D')
    if count<0:
        for y in range(0,abs(count)):
            s.append('U')
count1=0
count_counter=[None]*(len(s)+1)
count_counter[0]=0
j=0
for j in range(0,len(s)):
    count1=count1+dict2[s[j]]
    count_counter[j+1]=count1
plt.plot(count_counter)
#count number the valleys
b = []
i=0
for i in range(1,len(count_counter)):
    if count_counter[i] == 0:  b.append(i)
p=0
v=0
if b==[]:
    if count_counter[2]<0:
        v=v+1
    if count_counter[2]>0:
        p=p+1
if b!=[]:
    t=0
    for t in range(1,len(count_counter)-1):
        if count_counter[t]>count_counter[t-1] and count_counter[t]>count_counter[t+1]:
            p=p+1
        if count_counter[t]<count_counter[t-1] and count_counter[t]<count_counter[t+1]:
            v=v+1