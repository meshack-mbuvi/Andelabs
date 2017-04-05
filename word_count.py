# -*- coding: utf-8 -*-
def words(string):
    """
    :Author: Mbuvi
    :http://mbuv.wordpress.com
    :Email: meshmbuvi@gmail.com
    :Argument: string
    :Return : dictionary
    This is a function that counts the frequency(number of occurrence) of
    words in a given sentence
    """
    new_list=[] #List to hold words in the sentence 
    string_dict={}#dictionary to hold the words and thier frequencies
    
    if type(string)==type(str()):
        #split the argument if it is a string
        new_list=string.split()
    elif type(string)==type(dict()):
        #Get the keys for words if the argument is a dictionary
        new_list=string.keys()        
    elif type(string)==type([]):
        #Use the argument the way it is if it is a list
        new_list=string
    #extract number values and string values seperately
    int_list=[int(x) for x in new_list if x.isdigit()]
    str_list=[str(x) for x in new_list if not x.isdigit()]
    """
        Count the words now
    """
    for word in int_list:
        if word in string_dict:
            string_dict[word]+=1
        else:
            string_dict[word]=1
    for word in str_list:
        if word in string_dict:
            string_dict[word]+=1
        else:
            string_dict[word]=1
    return string_dict

if __name__=='__main__':
    print words('testing 1 2 testing')