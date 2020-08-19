# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 14:19:18 2020

@author: Rbala
"""
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




    
    
    
    
    
    
    
    
    
    
