"""
Write a python program to store two points as tuple and calculate distance between them 
"""
import math as mt
x1,y1 = map(int, input("Enter tuple 1: ").split(','))
x2,y2 = map(int, input("Enter tuple 2: ").split(','))
tuple_1 = (x1,y1)
tuple_2 = (x2,y2)

distance = mt.sqrt((x2-x1)**2 + (y2-y1)**2)
print("Distance between the two points: ",distance)
