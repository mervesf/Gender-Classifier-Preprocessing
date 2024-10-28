# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 15:44:43 2023

@author: user
"""

import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
import string
import json


    
df=pd.read_csv('gender_classifier.csv',encoding = "latin1")
x=df.dropna(subset=['description'], axis=0)
word=pd.read_csv('unigram_freq.csv')
word.drop('count',axis=1,inplace=True)

    
#Delete all non-letters in DataCleaningDescription and make all letters lowercase.
def clean_(feature):
    feature=feature.astype('string')
    alfabeth=string.ascii_letters
    for i in feature.index:
        value=''
        for j in word_tokenize(feature[i]):
            print(j)
            for k in j:
                if k not in alfabeth:
                    j=j.replace(k,'')
            value=' '.join([value,j.lower()])
        feature[i]=value
# Dividing words into groups of 1, 2 and 3.

def token(feature):
    feature=feature.astype('string')
    list_1=[]
    list_2=[]
    bigram_list=[]
    trigram_list=[]
    for i in feature:
        list_1.append(word_tokenize(i)),
    for i in list_1:
        if len(i)<=2:
            list_2.append(np.array([i]))
        else:
            for j in range(0,len(i)-2):
                list_2.append(np.array([i[j],i[j+1]]))
        bigram_list.append(list_2)
        list_2=[]
    for i in list_1:
        if len(i)<=2:
            list_2.append(np.array([i]))
        else:
            for j in range(0,len(i)-3):
                list_2.append(np.array([i[j],i[j+1]]))
        trigram_list.append(list_2)
        list_2=[]
    return list_1,bigram_list,trigram_list
# Remove stop-words from sentences

def throw_stopwords(feature):
    with open('english.txt', 'r', encoding='utf-8') as file:
        file_1 = [word.strip() for word in file.readlines()]
    feature=feature.astype('string')
    for i in feature.index:
        value_=''
        for j in word_tokenize(feature[i].lower()):
            sonuc=True
            for k in file_1:
                if j==k:
                    sonuc=False
                    break
            if sonuc:
                value_=' '.join([value_,j])
        feature[i]=value_
    return feature

# Finding roots in sentences and replacing words with their roots
def lemmatizasyon(feature):
    with open('english.roots.list.build.json', 'r') as dosya:
        veri = json.load(dosya)
    feature=feature.astype('string')
    root_list=''
    for i in feature.index:
        for k in word_tokenize(feature[i].lower()):
            for root in veri.keys():
                sonuc=False
                if len(k)>=len(root):
                  for j in range(0,len(k)-len(root)+1):
                          if root==k[j:j+len(root)]:
                              sonuc=True
                              root_list=' '.join([root_list,root])
                              break
                else:
                    root_list=' '.join([root_list,k])
                if sonuc:
                    break
                

                     
# Divide the paragraph into sentences according to the points
def sentences(text):
    indis=[i for i in range(0,len(text)) if text[i]=='.']
    rate=0
    sayac=0
    text_1=[]
    while sayac<len(indis):
        rate_1=indis[sayac]
        text_1.append(text[rate:rate_1])
        rate=indis[sayac]+1
        sayac+=1
    return text_1

#Divide each sentence in a paragraph according to its words
def split_1(text):
    split=[]
    split_text=[]
    for i in range(0,len(text)):
        if (text[i]==' ') or (text[i] in string.punctuation):
            if split:
                split_text.append(''.join(split))
            if text[i]!=' ':
                split_text.append(text[i])
            split=[]
        elif (text[i]!=' '):
            split.append(text[i])
            if (i==len(text)-1):
                split_text.append(''.join(split))
    return split_text








        
            
                

                
                  
                      
    
    





    


        

            
            