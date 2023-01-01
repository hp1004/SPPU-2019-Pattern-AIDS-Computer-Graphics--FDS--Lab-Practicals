''' Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string '''



# a) To display word with the longest length
""" def LongestWordLength(string):
    l=0
    w=" "
    words=string.split()
    for word in words:
        if (len(word)>1):
            w=word
            l= len(word)
    return (w,l)
string=input("Enter the string: ")
w,l=LongestWordLength(string)
print ("Longets Word is: ",w)
print ("Length of longest word is : ",l) """
string=input("Enter string")
list=[]
list=string.split()
print (list)

max_length=0
max_length_word=0
i=0

for i in range(len(list)):                                                  
    if len(list [i]) > max_length:
        max_length=len(list [i])
        max_length_word=list[1]
print(f"the word with longest length is: ", max_length_word)
print(f"Longest word length is: {max_length}")

# b) To determines the frequency of occurrence of particular character in the string
def freq(string1):
    d=dict()
    for c in string1:
        if c in d:
            d[c]=d[c]+1
        else:
            d[c]=1
    print(d)
string1=input("Enter the string: ")
print("------Frequency of each characters--------")
d=freq(string1)

#c) To check whether given string is palindrome or not
def palindrome(string2):
    rev=reversed(string2)
    if list(string2)==list(rev):
        print("String is palindrome...")
    else:
        print("string is not palindrome")
string2=input("Enter the string: ")
palindrome(string2)

# d) To display index of first appearance of the substring
string3=input("Enter the string: ")
sub_string=input("Enter substring: ")
index=string3.find(sub_string)
print(index)

# e) To count the occurrences of each word in a given string 
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
str=input("enter the string: ")
print( word_count(str))

