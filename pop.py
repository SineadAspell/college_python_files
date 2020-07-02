# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:47:22 2020

@author: Sinead
"""


# Python program showing pop() method 
# and remaining list after each pop 
  
list1 = [ 1, 2, 3, 4, 5, 6 ] 
print('Original list', list1) 
print('\n\n') 
# Pops and removes the last  
# element from the list 
print(list1.pop(), list1) 
  
# Pops and removes the 0th index 
# element from the list 
print(list1.pop(0), list1) 