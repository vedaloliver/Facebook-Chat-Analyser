import json
import pdb
import random
from collections import Counter
from datetime import datetime
from nltk import ngrams
import os.path
from pathlib import Path


path_dir = os.path.join("JSON_Files","Sam")
json_files = [pos_json for pos_json in os.listdir(path_dir) if pos_json.endswith('json')]

json_text_list = []

for index, js in enumerate(json_files):
    with open(os.path.join(path_dir, js), "r") as json_data:
        json_text_list.append(json.load(json_data))
#with open('message_1.json') as json_data:

jsondata2 = []
for i in range(len(json_text_list)):
    jsondata2 +=(json_text_list[i]['messages'])


def Info_to_Dict(doc):
# putting it all into lists do merge
    Name = []
    Content = []
    Timestamp = []
    # * unpacks it, reversing down by 1
    Dict_key = [*range(len(doc), -1,-1)]
    # adds to above empty lists
    for i in (range(len(doc))):
        Name.append(doc[i]['sender_name'])
        Content.append(doc[i].get('content'))
        Timestamp.append(doc[i].get('timestamp_ms'))
    #list which is going to be the values (name,content, etc)
    Dict_values_list = (list(zip(Name,Content,Timestamp)))
    Dict_comp = (dict(zip(Dict_key,Dict_values_list)))

    return Dict_comp
#messages master
Messages = (Info_to_Dict(jsondata2))

def phrase_frequency(dicts):
    # should have n changeable by an input parameter
    freq = ''
    for msg in range(1, len(dicts), 1):
        if isinstance(dicts[msg][1], str) == True:
            freq += (Messages[msg][1] + ' ')

    print ("""Do you want to see a list of all the most said words, or do you want to check how many times a 
    phrase has been said?

    1 : List

    2 : Phrase Check
    """)

    choice = int(input())
    n = 0
    p = ''
    c = choice == 1
    
    if choice == 1:
        print ("How many words do you want to see in a sequence? ")
        n = int(input())
    elif choice == 2 :
        print ("Please input the phrase to see how many times it has been said. ")
        p = input().lower()
        n = len(p.split())
    else :
        print ("Incorrect entry. Please try again")
    
    phrase_list = []
    phrase_list_updated = []
    bigrams = ngrams(freq.split(), n)
    for gram in bigrams:
        phrase_list.append(str(gram))      
        
    for i in phrase_list:
        phrase_list_updated.append(i.replace("'","").replace("(",'') 
        .replace(")",'').replace(",",''))

    def freq_count(lists):
        list_freq = {}
        for item in lists:
            if (item in list_freq):
                list_freq[item] += 1
            else: 
                list_freq[item] = 1

        if p != (''):
            for i in sorted(list_freq, key=list_freq.get, reverse=True):
                if p == i:
                    print ("The word: ", i, " Has been said ", list_freq[i], "times")
                           
        from Junk_words import remove_shit
        for w in sorted(list_freq, key=list_freq.get, reverse=True):
            if c and (n == 1):
                if list_freq[w] > 1000 and w not in remove_shit:
                    print (w, ": ", list_freq[w])
            elif c and (n == 2):
                if list_freq[w] > 100:
                    print (w, ": ", list_freq[w])
            elif c and (n == 3):
                if list_freq[w] > 25:
                    print (w, ": ", list_freq[w])
            elif c and  (n == 4):
                if list_freq[w] > 10:
                    print (w, ": ", list_freq[w])
            elif c and (n) >= 5:
                if list_freq[w] > 2:
                        print (w, ": ", list_freq[w])
            

    freq_count(phrase_list_updated) 

def recipient_frequency(dicts):
    messages_freq = []
    for i in range(1, len(dicts), 1):
        messages_freq.append(dicts[i][0].split(' ')[0])


    #print (messages_freq)
    def messages_freq_count(lists):
        list_freq = {}
        for item in lists:
            if (item in list_freq):
                list_freq[item] += 1
            else: 
                list_freq[item] = 1

        print (list_freq)
    messages_freq_count(messages_freq)

def get_time(dicts):
    times = []
    timeset = ''
    print ('press H for hour frequency, M for Month frequency or Y for Year frequency.')
    x = input().lower()
    if x == 'h':
        for msg in range(1, len(dicts), 1):
            times.append((datetime.fromtimestamp(int(str(dicts[msg][2])[:-3]))).hour) 
    elif x == 'm':
        for msg in range(1, len(dicts), 1):
            times.append((datetime.fromtimestamp(int(str(dicts[msg][2])[:-3]))).month)  
    elif x == 'y':
        for msg in range(1, len(dicts), 1):
            times.append((datetime.fromtimestamp(int(str(dicts[msg][2])[:-3]))).year)
    else:
        print ('Not a valid entry. Please try again')
    
    def freq_count(lists):
        list_freq = {}
        for item in lists:
            if (item in list_freq):
                list_freq[item] += 1
            else: 
                list_freq[item] = 1

        for w in sorted(list_freq, key=list_freq.get, reverse=True):
                print (w, ": ", list_freq[w])

    freq_count(times)

phrase_frequency(Messages)
#recipient_frequency(Messages)
#get_time(Messages)
