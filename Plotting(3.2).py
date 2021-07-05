# importing the libraries
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
%matplotlib inline
def freq():
#creating the list to store the results
    with open('sequence.txt', 'r') as file:
    # Converted the text file in to a list
          data = file.read().replace('\n', '').replace(',','').replace('[','')
    # created a function to convert the file
    def convert(string):
        list1 = []
        #created an empty list 
        #https://stackoverflow.com/questions/5764782/iterate-through-pairs-of-items-in-a-python-list
        for previous, current in zip(string, string[1:]):
            #merging two letters together and saving it in a list
            list1.append(previous+current)
        #returning the list
        return list1
#plotting the graph
#https://stackoverflow.com/questions/28418988/how-to-make-a-histogram-from-a-list-of-strings-in-python
    #counting the number of letters in the file
    letter_counts = Counter(convert(data))
    #generating data for the graph
    df = pd.DataFrame.from_dict(letter_counts, orient='index')
    #declaring type of graph
    df.plot(kind='bar')
    #label for the letter
    plt.xlabel('Nucleotide')
    #label for the frequency
    plt.ylabel('Frequency')
    #heading of the graph
    plt.title('Histogram of Virus')
    
#calling the function
freq()
