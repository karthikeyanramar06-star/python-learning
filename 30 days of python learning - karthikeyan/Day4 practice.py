#falsy comparison statement
a =  str("python")
b = str("dragon")
print(len,a)
print(len,b)
print(a == b ) 


#charachter finder  
c = "python"
d = "dragon"
if "on" in c and "on" in d:
     print(True)

#check if jargon is in the sentence
e = "I hope this course is not full of jargon"
if "jaogon" in e:
     print(True)

# type '10' = type 10
t ='10'
u = 10
print(type(t))
print(type(u))
if (type(t) == type(u)):
     print(True)
else:
     print(False)

#Check if int('9.8') is equal to 10
v = int(float('9.8'))
n = 10
if v == n:
     print(True)
else:
     print(False)\
     
#salarycalculator
Name = input("Enter your name: ",)
Hours = int(input("Enter your hours of work: ",))
Rate_per_hour = int(input("Enter your rate per hour: ",))
Your_weekly_earning = Hours*Rate_per_hour
print(Your_weekly_earning )

#living seconds calculator(no of days lived)
no_of_years_lived = int(input("Enter the no of years you lived: "))
year = 31536000
total_seconds_lived = no_of_years_lived * year
print("Total no of seconds lived: ", total_seconds_lived)

#Display the following numbers 1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125
print (1,1,1,1,1)
print (2,1,2,4,8)
print (3,1,3,9 ,27)
print (4,1,4,16,64)
print (5,1,5,25,125)