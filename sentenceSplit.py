'''
Created on 3 Feb 2016

@author: sapna
'''
import nltk
import csv
import re
import sys

from pip._vendor.distlib.util import CSVReader
from nltk.tokenize import word_tokenize    
def sentenceSplit(text):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(text)
    return sentences
def taggingNLTK(self, text):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(text)
    for sent in sentences:
        text = word_tokenize(sent)
        tagged_sent = nltk.pos_tag(text)
fileNames = ["abortion","creation","gayRights","god","guns","healthcare"]
for i in range(len(fileNames)):
    fileRead = open("C:/Python34/mergeDebates/" + fileNames[i] + ".csv","rU")
    csvFile = csv.writer(open("C:/Python34/mergeDebates/" + fileNames[i] + "Split.csv", "w",newline=''))
    with fileRead as tsvfile:
        tsvreader = csv.reader(tsvfile)
        id = 1
        for lines in tsvreader:
            text = lines[1]
            #print(text)
            try:
                sentences = sentenceSplit(text)
                #print(sentences[0])
                id2 = 1
                for sentence in sentences:
                    #print(sentence)
                    sentenceid = str(id)+"_"+ str(id2)
                    csvFile.writerow([sentenceid,sentence])
                    id2 +=1 
            except:
                #print ("error:",sys.exc_info()[0])
                pass
            int(id)
            id +=1       
print('Done!')
