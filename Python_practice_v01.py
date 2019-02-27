#def add(first, second):
#	total = first + second
#	return total
#print ("pogram begins from here")
#
#gettotal = add(10,20)
#print("sum of the numbers :", gettotal)
#
#def add(first, second):
#	total = first + second
#	return total
### calling function 
#gettotal = add(first =10 , second = 20)
#
#
#def display (*data):
#    print (set(data))
#    for item in data:
#        print(item)

#display (10,20,30,40,50,60,70,80,90)

#fobj = open("C:\\Users\\gsahoo\\OneDrive - Schlumberger\\Documents\\demo1.txt" , "w")
#fobj.write("python programming\n")
#fobj.write("ruby programming\n")
#fobj.write("scala programming\n")
#
#fobj.close()

#WAP o/p file
#fobj = open("C:\\Users\\gsahoo\\OneDrive - Schlumberger\\Documents\\demo1.txt" , "w")
#fobj.write("python programming\n")
#fobj.write("ruby programming\n")
#fobj.write("scala programming\n")
#
#fobj.input("Add some text")
#
#fobj.close()

#WAP to all odd no. from 700 to 400 to the file and the file name should be
#with todays timestamp
#read lin eby line
#fobj = open ("languages.txt", "r")
#for line in fobj:
#    print(line)
#fobj.close()

#fobj = open ("C:\\Users\\gsahoo\\OneDrive - Schlumberger\\Desktop\\.txt", "r")
#for line in fobj:
#    #remove the whitespace at the end of each line
#    line = line.strp()
#    #spilt the line with, as the delimeter
#    data = line.split(",")
#    print(data[0])
#fobj.close()
#
#fobj = open ("C:\\Users\\gsahoo\\datasets\\employees.csv", "r")
#
##File reading from desktop
#for line in fobj:
##    line = line.strip()
#   if  "Female" in line :
#    print(line)
#fobj.close()

#How to write the Data
 
#fobj=open(r"C:\Users\vmirje\Desktop\Python Scripting Trainig\Day 2\git\datasets\employees.csv",'r')
#fobj1=open(r"C:\Users\vmirje\Desktop\Python Scripting Trainig\Day 2\git\datasets\employees_copy.csv",'w')
#for line in fobj:
#    fobj1.write(line)
#fobj1.close()
#fobj.close() 
#WAP a program to display the count of male and female employee
#
# WAP to display the lines where the salary > 100000
# WAP a program to read the file and replace the lines conatining "business Development" to "information technology "
# and write the output tp other file.
 
#fobj = open ("C:\\Users\\gsahoo\\datasets\\employees.csv", "r") 
#Fcount = 0
#Mcount = 0
#
#for line in fobj:
#    line = line.strip()
#    data = line.split(",")
#    if data[1] == "Female":
#        Fcount = Fcount + 1 
#    elif data[1] == "Male":
#        Mcount = Mcount + 1 
#        
#        
#        
#print ("Female employee total", Fcount)
#print ("Male employee total", Mcount)
#    
##fobj.close()
##==================================
#fobj = open ("C:\\Users\\gsahoo\\datasets\\employees.csv", "r") 
#Fcount = 0
#Mcount = 0
#Sal = 'A'
#sal = A[4]
#for line in fobj:
# A = line.split(",")
#if int(sal [4] > 100000) :
#    print(line)
#
#    fobj.close()

#import os 
#print(os.listdir())

#Link to Delete
#
#https://stackoverflow.com/questions/43756284/how-to-remove-a-directory-including-all-its-files-in-python
#
# 
##Size of the File 
#import os
#print os.path.getsize('mydata.csv')
#print os.stat('mydata.csv').st_size

 #os.getlogin
 
fobj = open ("C:\\Users\\gsahoo\\datasets\\employees.csv", "r")

#File reading from desktop
for line in fobj:
   line = line.strip()
data = line.split(",")
print(data[0])
fobj.close()

import csv
     with open(""employees.csv) as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print(line)


 

