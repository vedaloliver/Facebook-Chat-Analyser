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