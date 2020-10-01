import json
import pdb
import random
import os.path
from collections import Counter
from datetime import datetime
from nltk import ngrams
from pathlib import Path
total_participants= {}
Messages = {}

def init():
    #Gathers the inserted files and processes them for reading by subsequent functions
    global Messages
    def json_combine():
        #Longer chats will have a greater number of files present, this is responsible for the combination into one main file
        json_text_list = []
        jsondata2 = []
        json_files = [pos_json for pos_json in os.listdir() if pos_json.endswith('json')]

        for index, js in enumerate(json_files):
            with open(os.path.join( js), "r") as json_data:
                json_text_list.append(json.load(json_data))

        for i in range(len(json_text_list)):
            jsondata2 += (json_text_list[i]['messages'])

        return jsondata2
    
    def Info_to_Dict(doc):
        #Unpacks the json data into a Dictionary for legibility
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


    Messages = (Info_to_Dict(json_combine()))
    return Messages


def phrase_frequency(dicts):
    #This shows who is present in the chat, and prompts the user if they want to see phrase frequency on one individual or all of the chat
    #Will subsequently ask if:
    ## they want to see a list of most said words/phrases (user can choose n words to show phrase frequency)
    ## They want to check how many times a specific word/phrase has been uttered 
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

    print("""
    Do you want to see a list of all the most said words, or do you want to check how many times a 
    phrase has been said?\n\n    1 : List\n\n    2 : Phrase Check""")

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
                print(w, ": ", dicts[w])
                count += 1
                if count == 25:
                    break

        def display_single(dicts):
            if p != (''):
                for i in sorted(dicts, key=dicts.get, reverse=True):
                    if p == i and n > 1:
                        print("The phrase:", i, "Has been said",
                              dicts[i], "times.")
                    if p == i and n == 1:
                        print("The word:", i, "Has been said",
                              dicts[i], "times.")

        if choice == 1:
            display_list(list_freq)
        elif choice == 2:
            display_single(list_freq)

    freq_count(str_to_list(Which_freq)),end_choices()


def recipient_frequency(dicts):
    #Relatively simply shows who is present in the chat, and the amount of messages they have sent
    # also includes a proportion , but this is not working correctly
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
                print ("Below is a list of message frequency of the recipients in the chat, in descending order: \n")
                for i in sorted(list_freq_x, key=list_freq_x.get, reverse=True):
                        print(i, ": ", list_freq_x[i])
                                

                print("\n This would give the participants", ", ".join(names[:-1]),"and", str(names[-1]) , " a message proportion of",
                  ":".join(values_ratio), ", Respectively.\n _______________________________________")

            elif len(names) == 2:
                print("There are", len(names), "participants in the chat.")
                print(" and ".join(names), "have sent", " and ".join(
                   valuess), 'messages, Respectively.\n')
                print("They would give them a message proportion of",
                  " : ".join(values_ratio), ".\n")

            #print(len(names))
        freq_disp(list_freq_x)
    messages_freq_count(messages_freq), end_choices()

   
def get_time(dicts):
    #Provides information for when the messages have been sent
    #An issue has arose about the Hour frequency - i am suspecting it may be due to a different time zone i am in affecting this.
    print('\n press H for hour frequency, M for Month frequency or Y for Year frequency.\n')
    x = input().lower()

    def time_chooser(timez):
        times = []
        timeset = ''
        if timez == 'h':
            print('Below is the frequency of messages sent, organized by hour:')
            for msg in range(1, len(dicts), 1):
                times.append((datetime.fromtimestamp(
                    int(str(dicts[msg][2])[:-3]))).hour)
        elif timez == 'm':
            print('Below is the frequency of messages sent, organized by month:')
            for msg in range(1, len(dicts), 1):
                times.append((datetime.fromtimestamp(
                    int(str(dicts[msg][2])[:-3]))).month)
        elif timez == 'y':
            print('Below is the frequency of messages sent, organized by year:')
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

    time_chooser(x),end_choices()
    


def end_choices():
    # gives the user a choice to go back and repick another category or exit the program
    while True:
        print('\n\nMain menu = 1, Exit program = 2')
        end_choice = ((input()))
        if end_choice == str(1):
            choice()
        elif end_choice == str(2):
            print('Program terminated.')
            break
        else:
            print("Invalid input. Please try again.")

def choice():
    #Essentially starts the program and allows the individual to have choice in what they want to see
    choice = 0
    print('Welcome to the facebook chat analyser. Information for the retrieval of your chat data is available on the readme.\n')
    while True:
        print('Phrase Frequency = 1\n\nRecipient Frequency = 2\n\nTime Statistics = 3: \n\nExit Program = 4:')
        choice = ((input()))
        if choice == str(1):
            phrase_frequency(Messages)
            break
        elif choice == str(2):
            recipient_frequency(Messages)
            break
        elif choice == str(3):
            get_time(Messages)
            break
        elif choice == str(4):
            print('\nProgram terminated.\n')
            break
        else:
            print("Invalid. Please try again.")


init()
choice()




