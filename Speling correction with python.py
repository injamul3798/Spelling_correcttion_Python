#Import Library
from textblob import TextBlob

#Create a list with wrong word
word = ["Data Scence", "Mahine Learnin","Data Scientis"]
correct_word = []   #will store correct word
for i in word:
    #storing correct word into correctZ_word
    correct_word.append(TextBlob(i))
    
print("Given wrong words: ",word);
print('Correct words are: ')
for i in correct_word:
    print(i.correct(),end=' ')
    
    
'''
Output: 
Given wrong words:  ['Data Scence', 'Mahine Learnin', 'Data Scientis']
Correct words are: 
Data Science Machine Learning Data Scientist '''


