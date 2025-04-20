import random

print("Random Integer=",random.randint(30,70))
cities=["Bengaluru","Mumbai","Chennai","Delhi","Kolkata"]
print("Random City=",random.choice(cities))

dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]
for i in range(0,5):
    random.shuffle(dice1)
    random.shuffle(dice2)
print("Random numbers from two dices = ",random.choice(dice1),",",random.choice(dice2))


import time

print("Local time=",time.ctime(1603436)) #Seconds passed since epoch
time.sleep(3)
print("Printed after 3s")

import datetime

print("DateTime=",datetime.datetime.now())
print("Date=",datetime.date.today())

import math

n2=int(input("Enter a number="))
print("It's factorial=",math.factorial(n2))
print("It's power 3=",math.pow(n2,3))


import mypackage.module1 as module1
import mypackage.module2 as module2
import mypackage.module3 as module3

print("Module1=",module1.greet("Manas"))
print("Module2=",module2.square(10))
print("Module3=",module3.multiply(6, 7))


file1=open("test.txt","w")
file1.write("-------------\n")
file1.write("Hello World\n")
file1.close()
print("Text file created")
with open("test.txt","r") as file:
    content=file.readlines()
    print(content)

from zipfile import *
f=ZipFile("test.zip",'w',ZIP_DEFLATED)
f.write("test.txt")
f.close()
print("Zip file created ")

import os
print("Current directory=",os.getcwd())

from mypackage import greet, multiply

print(greet("All"))
print(multiply(4, 3))







