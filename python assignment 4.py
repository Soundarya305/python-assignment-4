#!/usr/bin/env python
# coding: utf-8

# In[4]:


###1.1 write a python program(with class concepts) to find the area of the triangle using the below formula.
##area=(s*(s-a)*(s-b)*(s-c))**0.5. Function to take the length of the sides of triangle should be defined in the parent class and function to calculate the area should be defined in subclass.

class poly:
    def __init__(self, a, b, c):
        self.a= float(a)
        self.b= float(b)
        self.c= float(c)
a= int(input("a="))
b= int(input("b="))
c= int(input("c="))

class triangle(poly):
    def __init__(self, a, b, c):
        super().__init__( a, b, c)
        
    def get_area(self):
        s= (self.a + self.b + self.c ) / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
    
t = triangle(a,b,c)
print("area : {}".format(t.get_area()))


# In[6]:


###write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are no longer than n
def filter_long_words(i,a):
    words=[]
    for j in i:
        if(len(j)>=a):
            words.append(j)
    return words

n=input("Enter words:")
nt=n.split(",")
na=input("Enter min length:")
long=filter_long_words(nt,int(na))

print("words with atleast min length:",long)


# In[3]:


###2.1 write a python program using function concept that maps lists of words into a list of integers presenting the lengths of the corresponding words

def find_length(list_1):
    new_list=[]
    for i in range (0,len(list_1)):
        new_list.append(len(list_1[i]))
    return new_list
list_2=['ab','cde','erty']
length_lst=find_length(list_2)
print(length_lst)


# In[3]:


###2.2 write a python program function which takes a character (i.e. a string of length 1) and returns true if it a vowel and false otherwise
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('s'))
print(is_vowel('a'))


# In[ ]:




