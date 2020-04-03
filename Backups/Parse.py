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
print (json_files)

json_text_list = []

for index, js in enumerate(json_files):
    with open(os.path.join(path_dir, js), "r") as json_data:
        json_text_list.append(json.load(json_data))
#with open('message_1.json') as json_data:

    jsondata2 = []
    for i in range(len(json_text_list)):
        jsondata2 +=(json_text_list[i]['messages'])


    print(len(jsondata2))


    


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
    def word_frequency(dicts):
        messages = ''
        message_list = []
        for msg in range(1, len(dicts), 1):
            if isinstance(dicts[msg][1], str) == True:
                messages += (Messages[msg][1] + ' ')
        
        message_list = messages.split(' ')
        #print (message_list)
        def str_to_freq_dict(lists):
            list_freq = {}
            for item in lists:
                if (item in list_freq):
                    list_freq[item] += 1
                else: 
                    list_freq[item] = 1
            
            
            from Junk_words import remove_shit

            def misc_word_remove(entries,the_dict):
                for i in remove_shit:
                    if i in the_dict:
                        del the_dict[i]
        
            misc_word_remove(remove_shit, list_freq)    
        
            for w in sorted(list_freq, key=list_freq.get, reverse=True):
                if list_freq[w] > 100 :
                    print (w, ": ", list_freq[w])
            
            print ("Check a word to see how many times it's been said!")
            x = input().lower()
            if x in list_freq.keys():
                print ("Yes, '", x, "' is in the dictionary")
                print (str(x) + " has been mentioned " + str(list_freq.get(x)) + " times.")
            elif x in remove_shit:
                print(str(x)+ "Has been removed from analysis as it's junk/common. Try another!")
            else : 
                print ("No, '", x, "' is not  present.")

        print (str_to_freq_dict(message_list))  

    def two_word_phrase_frequency(dicts):
        # should have n changeable by an input parameter
        two_word_freq = ''
        for msg in range(1, len(dicts), 1):
            if isinstance(dicts[msg][1], str) == True:
                two_word_freq += (Messages[msg][1] + ' ')

        n = 2
        phrase_list = []
        phrase_list_updated = []
        bigrams = ngrams(two_word_freq.split(), n)
        for gram in bigrams:
            phrase_list.append(str(gram))      
            
        for i in phrase_list:
            phrase_list_updated.append(i.replace("'","").replace("(",'') 
            .replace(")",'').replace(",",''))

        def two_word_freq_count(lists):
            list_freq = {}
            for item in lists:
                if (item in list_freq):
                    list_freq[item] += 1
                else: 
                    list_freq[item] = 1

            for w in sorted(list_freq, key=list_freq.get, reverse=True):
                if list_freq[w] > 5:
                    print (w, ": ", list_freq[w])

        two_word_freq_count(phrase_list_updated) 

    def recipient_frequency(dicts):
        messages_freq = []
        for i in range(1, len(dicts), 1):
            messages_freq.append.lower((((dicts[i][0].split(' ')[0]))))
        print (messages_freq)
        def messages_freq_count(lists):
            list_freq = {}
            for item in lists:
                if (item in list_freq):
                    list_freq[item] += 1
                else: 
                    list_freq[item] = 1

            print (list_freq)
        messages_freq_count(messages_freq)

    def get_hour(dicts):
        times = []
        # converts to datetime from timestamp. 3 extra numbers on fb timestamp make it confused
        # removing the last three digits allow for proper use, but req conv to str and int (sloppy)
        #num =  
        #print (num.hour)
        for msg in range(1, len(dicts), 1):
            times.append((datetime.fromtimestamp(int(str(dicts[msg][2])[:-3]))).hour)   
        
        def hour_freq_count(lists):
            list_freq = {}
            for item in lists:
                if (item in list_freq):
                    list_freq[item] += 1
                else: 
                    list_freq[item] = 1

            for w in sorted(list_freq, key=list_freq.get, reverse=True):
                    print (w, ": ", list_freq[w])

        hour_freq_count(times)
   
    def get_month(dicts):
        months = []

        for msg in range(1, len(dicts), 1):
            months.append((datetime.fromtimestamp(int(str(dicts[msg][2])[:-3]))).month)

        def month_freq_count(lists):
            list_freq = {}
            for item in lists:
                if (item in list_freq):
                    list_freq[item] += 1
                else: 
                    list_freq[item] = 1

            for w in sorted(list_freq, key=list_freq.get, reverse=True):
                print (w, ": ", list_freq[w])

        month_freq_count(months)

    def get_year(dicts):
        years = []

        for msg in range(1, len(dicts), 1):
            years.append((datetime.fromtimestamp(int(str(dicts[msg][2])[:-3]))).year)

        def year_freq_count(lists):
            list_freq = {}
            for item in lists:
                if (item in list_freq):
                    list_freq[item] += 1
                else: 
                    list_freq[item] = 1

            for w in sorted(list_freq, key=list_freq.get, reverse=True):
                print (w, ": ", list_freq[w])

        year_freq_count(years)
 
    #word_frequency(Messages)
    #two_word_phrase_frequency(Messages)
    #recipient_frequency(Messages)
    #get_hour(Messages)
    #get_month(Messages)
    #get_year(Messages)
    