# looking at file handling in python
import pylab as pl
import numpy as np
import matplotlib as mtplt
import factorial as f

name = open("new.txt", "w")

for i in range(0, 1):
    digit = int(input("Enter the Digit\t"))
    digit_2 = int(input("Enter the Digit\t"))
    print("\n")
    name.write("Line %d -> %d + %d = %d \n" %(i, digit, digit_2, f.factorial(digit)+f.factorial(digit_2)))
name.close()

nam = open("new.txt", "r")
string = nam.read()
line = nam.readline()
print(line)
print("The Numbers entered are\n\n",string)
nam.close()