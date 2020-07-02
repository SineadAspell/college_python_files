# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def h_Calculator(datasize): # function for h and to check that they are equal
    
    increment= datasize[1] - datasize[0] 
    for i in range(1, len(datasize)):
        if not datasize[i] - datasize[i -1] == increment: #if h is not equal
            return False 
    return float(increment)
    

def Simpson(x_data, y_data): #function for simpson rule
    even=0 #variable for even
    odd=0 #variable for odd
    h = h_Calculator(x_data) #variable for h
    
    for i in range(1, len(y_data)-1):
        if i % 2==0: #checks if even
            even += y_data[i] #adds even values to even variables
        else:
            odd += y_data[i] #adds odd values to odd variables
        #if x is valid calculation occurs  
        return "Error" if h == False else(1/3) * (h*(y_data[0]+(4*odd)+(2*even) + y_data[-1])) # returns error message if x data is invalid

datasize_len = int(input("Data size: ")) # inputs datasize
while datasize_len % 2 ==0: # while datasize is valid
    datasize_len= int(input("Data size: "))
    
x_datasize = [float(input(f"Enter number x {i+1}: ")) for i in range(datasize_len)] #creates x values
                         
y_datasize=[float(input(f"Enter number y {i+1}: ")) for i in range(datasize_len)] #creates y values


Answer= Simpson(x_datasize, y_datasize)
print("Answer: ", Answer) # prints the answer