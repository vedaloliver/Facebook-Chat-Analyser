# My first project : A Simple Facebook Scraper

This was the first project i have worked on, so it is a little bit rudimentary in complexity and algorithmic cleanliness.

Inspiration for this project came from the understanding that it was possible to gather all of my past facebook chat data. With vastly large amounts of data presented to the individual, it was only viable to construct a script to gather and understand certain trends in my conversational data.

____________________________________________________________________________

This was created to both test and display a number of competencies i have been learning, such as:

- General algorithmic complexity
- use of JSON parsing/scraping to gather necessary data
- Visaul representation of  data using packages such as Matplotlib

___________________________________________________________________________________________________

Various functions include:

1.  Frequency of recepients in a given chat
- this allows the user to gather data from any chat, either a 2 person chat, or a large, multi person conversation.
- This gives both the number of messages and the message proportion, showing who has spoken the most or the least.

2. Frequency of mentioned words or phrases
This function allows the user to either:
- A: See a chat participants most frequent words or phrases mentioned. The user will be promted to give a number, which represents how many words will be in the sequence - for example, 3 will produce the most 3 word phrases in the text, such as 'I love you'.
- B: Gives the opportunity for the user to input a phrase, to see how many times the word or phase has been mentioned in the chat.

3. Time frequencies
This gives the user to find out the most frequent time for each message in the chat, giving the opportunty to produce
- A: Frequency by Hour
- B: Frequency by Month
- C: Frequency by Year

__________________________________________________________________________________________
How to :

Your information is freely available to request from facebook, and may be located at this link :
- https://www.facebook.com/dyi/?referrer=ayi

Once you have directed youself to the link, select only the 'Messeges' to be requested. For compatibility with the project, the format of the file must be JSON. Once requested, Facebook will notify you within 1-3 days that the files are available to you.

Once this is complete, locate the folder and add it to the directory of this project. input will request for a file name to provide.



___________________________________________________________________________________________
I Currently regard this project as unfinished, and would need to go back and add complexity and clean up the code.

To do:

- Add input to gather the file name of the chat. this will be different for a single file or for a multi file chat
- clean up the code, better nest everything into functions 
- choice function to choose what function they want to select 
