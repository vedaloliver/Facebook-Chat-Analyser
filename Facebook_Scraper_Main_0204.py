import json
import pdb
import random
import os.path
from collections import Counter
from datetime import datetime
from nltk import ngrams
from pathlib import Path
from Junk_words import remove_shit


path_dir = os.path.join("C:\\", "Users", "Oliver", "Desktop",
                        "Code_Files", "Facebook_Scraper", "JSON_Files", "fam")


json_files = [pos_json for pos_json in os.listdir(
    path_dir) if pos_json.endswith('json')]

json_text_list = []
jsondata2 = []
total_participants= {}




for index, js in enumerate(json_files):
    with open(os.path.join(path_dir, js), "r") as json_data:
        json_text_list.append(json.load(json_data))

for i in range(len(json_text_list)):
    jsondata2 += (json_text_list[i]['messages'])


def Info_to_Dict(doc):
    Name = []
    Content = []
    Timestamp = []
    # * unpacks it, reversing down by 1
    Dict_key = [*range(len(doc), -1, -1)]
    for i in (range(len(doc))):
        Name.append(doc[i]['sender_name'])
        Content.append(doc[i].get('content'))
        Timestamp.append(doc[i].get('timestamp_ms'))

    Dict_values_list = (list(zip(Name, Content, Timestamp)))
    Dict_comp = (dict(zip(Dict_key, Dict_values_list)))

    return Dict_comp


Messages = (Info_to_Dict(jsondata2))


def phrase_frequency(dicts):
    global total_participants

    print(""" 
    Next, Input the name of who's word or phrase frequency you want to see. 

    Incorrect input will result in showing frequencies for all parties in the chat
    """)
    participant = input().lower()    
    alls = ""


    for i in range(1, len(dicts), 1):

        if (participant in total_participants.keys()) and(isinstance(dicts[i][1], str) == True) and participant in Messages[i][0].lower():
            total_participants[participant] += (Messages[i][1] + ' ')
        elif participant not in total_participants.keys() and (isinstance(dicts[i][1], str) == True):
            alls += (Messages[i][1] + ' ')
    
    if (participant not in total_participants.keys()):
        Which_freq = alls
    else:
        Which_freq = total_participants[participant]

    #print (Which_freq)


    print("""
    Do you want to see a list of all the most said words, or do you want to check how many times a 
    phrase has been said?

    1 : List

    2 : Phrase Check
    """)

    choice = int(input())
    n = 0
    p = ''
    c = (choice == 1)

    if choice == 1:
        print("How many words do you want to see in a sequence? ")
        n = int(input())
    elif choice == 2:
        print("Please input the phrase to see how many times it has been said. ")
        p = input().lower()
        n = len(p.split())
    else:
        print("Incorrect entry. Please try again")

    def str_to_list(strs):
        phrase_list = []
        phrase_list_updated = []
        bigrams = ngrams(strs.split(), n)
        for gram in bigrams:
            phrase_list.append(str(gram))

        for i in phrase_list:
            phrase_list_updated.append(i.replace("'", "").replace("(", '')
                                       .replace(")", '').replace(",", ''))

        return phrase_list_updated

    def freq_count(lists):
        list_freq = {}
        for item in lists:
            if (item in list_freq):
                list_freq[item] += 1
            else:
                list_freq[item] = 1

        def display_list(dicts):
            count = 0
            for w in sorted(dicts, key=dicts.get, reverse=True):
                if w not in remove_shit:
                    print(w, ": ", dicts[w])
                    count += 1
                    if count == 25:
                        break

        def display_single(dicts):
            if p != (''):
                for i in sorted(dicts, key=dicts.get, reverse=True):
                    if p == i and n > 1 and (i not in remove_shit):
                        print("The phrase:", i, "Has been said",
                              dicts[i], "times.")
                    if p == i and n == 1 and (i not in remove_shit):
                        print("The word:", i, "Has been said",
                              dicts[i], "times.")

        if choice == 1:
            display_list(list_freq)
        elif choice == 2:
            display_single(list_freq)

    freq_count(str_to_list(Which_freq))


def recipient_frequency(dicts):
    global total_participants
    messages_freq = []
    for i in range(1, len(dicts), 1):
        messages_freq.append(dicts[i][0].split(' ')[0])

    def messages_freq_count(lists):
        list_freq_x = {}
        for item in lists:
            if (item in list_freq_x):
                list_freq_x[item] += 1
            else:
                list_freq_x[item] = 1

        def freq_disp(dicts):
            global total_participants
            values = list(dicts.values())
            names = list(dicts.keys())
            values_ratio = []
            valuess = []


            for i in values:
                values_ratio.append(str((round(i/(sum(values))*100))))
                valuess.append(str(i))
            for i in names:
                total_participants.update({str(i).lower():'x'})

            if len(names) > 2:
                print ("There are", len(names), "participants in the chat.")
                print ("Below is a list of message frequency by recepient, in descending order: \n")
                for i in sorted(list_freq_x, key=list_freq_x.get, reverse=True):
                        print(i, ": ", list_freq_x[i])
                                

                print("\n This would give the participants", ", ".join(names[:-1]),"and", str(names[-1]) , " a message proportion of",
                  ":".join(values_ratio), ", Respectively.\n _______________________________________")

            elif len(names) == 2:
                print("There are", len(names), "participants in the chat.")
                print(" and ".join(names), "have sent", " and ".join(
                   valuess), 'messages, Respectively.\n')
                print("They would give them a message proportion of",
                  ":".join(values_ratio), ".\n")

            #print(len(names))
        freq_disp(list_freq_x)
    messages_freq_count(messages_freq)

   

def get_time(dicts):
    print('\n press H for hour frequency, M for Month frequency or Y for Year frequency.\n')
    x = input().lower()

    def time_chooser(timez):
        times = []
        timeset = ''
        if timez == 'h':
            for msg in range(1, len(dicts), 1):
                times.append((datetime.fromtimestamp(
                    int(str(dicts[msg][2])[:-3]))).hour)
        elif timez == 'm':
            for msg in range(1, len(dicts), 1):
                times.append((datetime.fromtimestamp(
                    int(str(dicts[msg][2])[:-3]))).month)
        elif timez == 'y':
            for msg in range(1, len(dicts), 1):
                times.append((datetime.fromtimestamp(
                    int(str(dicts[msg][2])[:-3]))).year)
        else:
            print('\n Not a valid entry. Please try again\n ')
        
        def freq_count(lists):
            list_freq = {}
            for item in lists:
                if (item in list_freq):
                    list_freq[item] += 1
                else:
                    list_freq[item] = 0

            def display(dicts):
                for w in sorted(dicts, key=dicts.get, reverse=True):
                    if timez == 'h':
                        if w >= 7:
                            print(w-7, ": ", dicts[w])
                        if w < 7:
                            print(24-(7-w), ": ", dicts[w])
                    else:
                        print(w, ":", dicts[w])
            display(list_freq)
        freq_count(times)

    time_chooser(x)

recipient_frequency(Messages)
phrase_frequency(Messages)
#get_time(Messages)
#print (total_participants)




