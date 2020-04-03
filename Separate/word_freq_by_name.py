import json,pdb,random,os.path
from collections import Counter
from datetime import datetime
from nltk import ngrams
from pathlib import Path

path_dir = os.path.join("JSON_Files","Sam")
json_files = [pos_json for pos_json in os.listdir(path_dir) if pos_json.endswith('json')]

json_text_list = []
jsondata2 = []

for index, js in enumerate(json_files):
    with open(os.path.join(path_dir, js), "r") as json_data:
        json_text_list.append(json.load(json_data))

for i in range(len(json_text_list)):
    jsondata2 +=(json_text_list[i]['messages'])

def Info_to_Dict(doc):
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
Messages = (Info_to_Dict(jsondata2))

#print (Messages[24])
def phrase_frequency(dicts):
    freq = ''
    for msg in range(1, len(dicts), 1):
        if isinstance(dicts[msg][1], str) == True:
            freq += (Messages[msg][1] + ' ')
    
    freq_1 = ''
    freq_2 = ''
    for msg in range(1, len(dicts), 1):
            if isinstance(dicts[msg][1], str) == True:
                if (dicts[msg][0]== str('Oliver Ward')):
                    freq_1 += (Messages[msg][1] + ' ')
                elif (dicts[msg][0]== str('Sam Well')):
                    freq_2 += (Messages[msg][1] + ' ')

    Which_freq = freq
    print (""" Input the name of who's word/phrase frequency you want to see. Incorrect input will result
    in showing for all parties in the chat
    """)
    participant = input().lower()
    if participant == 'oliver':
        Which_freq = freq_1
    elif participant == 'sam':
        Which_freq = freq_2


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
    bigrams = ngrams(Which_freq.split(), n)
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
                if p == i and n>1:
                    print ("The phrase:", i, "Has been said", list_freq[i], "times.")
                if p == i and n==1:
                    print ("The word:", i, "Has been said", list_freq[i], "times.")
                           
                           
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

print (phrase_frequency(Messages))