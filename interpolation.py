# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 14:12:55 2020

@author: Sinead
"""


def IntPol( x0,x1,x2,y0,y1,y2): #function for interpolation
    h=x1-x0 
    k=xbar-x0 
    delta0 = y1-y0
    delta1 = y2 - y1 
    theta=k/h
    ybar=y0+theta*delta0+((theta*(theta-1))/2)*(delta1-delta0)
    return ybar; #returns ybar



datasize = int(input('Enter how many x values to be inputed : ')) #inputs the data size
xbar = float(input('Enter xbar value:')) #input xbar
a = int(input('Enter the first point to be used:')) #0
b = int(input('Enter the second point to be used:')) #1
c = int(input('Enter the third point to be used:')) #2


x_set=[] #creates the x data set
y_set=[] #creates the y data set


for i in range(datasize): #In the range of datasize inputted
    x_set.append(float(input('Enter x: '))) #attaches x value to string x_dataset
    y_set.append(float(input('Enter y: '))) #attaches y value to string y_dataset
    
ybar = IntPol(x_set[a], x_set[b],x_set[c], y_set[a],y_set[b], y_set[c]) 
print('ybar:',ybar) #prints ybar 
