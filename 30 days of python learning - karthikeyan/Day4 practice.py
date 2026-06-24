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