#!/usr/bin/env python3

# Date = 18 Sept 2018
# Version = i
# OriginalAuthor = 

# Description: A program to model two speakers who exchange a "meaningful" conversation between each other. 

stopWords_list =["I", "have","know", "like", "love", " to ", " a "]
# we remove stop words as they do not add specificity to the strings

def removeStopWords(in_str):
    for s in stopWords_list:
        in_str = in_str.replace(s,"")
   # print("removeStopWords(), return statement: ",in_str,type(in_str) )
    return in_str.strip() # return the line without the stop words to the caller 
#end of removeStopWords()

def main():
    speakerAlice()
    speakerBob()
#TODO

#end of main()


def speakerAlice(): #you will need input parameters here
    print(" This is Alice!")
#TODO
#end of speakerA()

def speakerBob(): #you will need input parameters here
    print(" This is Bob!")
#TODO
#end of speakerA()


main() # runs the program 
