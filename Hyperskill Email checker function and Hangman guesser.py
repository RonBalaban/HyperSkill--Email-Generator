# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:19:18 2020

@author: Rbala
"""

# Shebang line for Windows is #!, followed by some info

#! python""3





def check_email(string):
    a = b = c = False
    # No spaces
    if ' ' not in string:
        a = True
    # contains @
    if '@' in string:
        b = True
    # . after @
    if '.' in string and string.rfind('.') > string.find('@') + 1:
        c = True
    if a and b and c:
        return True        
    return False






import random

words = ['python', 'java', 'kotlin', 'javascript']

# Write your code here
print("H A N G M A N")
correct_word = random.choice(words)
remaining = (len(correct_word) -3) * "-"
guess = input(f"Guess the word: {correct_word[0:3]}{remaining}  : ")
if guess == correct_word:
    print('You survived!')
else:
    print('You are hanged!')
    
    
    
    
    
    
    
    
    
    
    
    