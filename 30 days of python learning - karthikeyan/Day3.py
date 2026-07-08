#assignment operators 
a=3
b=4
c=6
d=7
a+=2
b-=4
c*=3
d/=9
print(a)
print(b)
print(c)
print(d)

# arithemetic operators
a-=10
b+=15
print(a)
print(b)

#calculation of area of circle,
#area of rectangle
#weight of an object
#Density of a liquid

radius = 20
pi = 3.14
area_of_circle= pi*radius**2
print('Area of circle:',area_of_circle)
length = 20
breadth = 10
area_of_rectangle=length*breadth
print("area of rectangle",area_of_rectangle)
mass = 20
gravity =9.81
weight_of_an_object=mass*gravity
print("Mass of an object:",weight_of_an_object)
mass=20
volume=40
density_of_a_liquid=mass/volume
print("Density of an volume:",density_of_a_liquid)
#check if jargon is in the sentence
e = "I hope this course is not full of jargon"
if "jargon" in e:
     print("Jargon is in the sentence :",True)

#There is no 'on' in both dragon and python
a = "dragon"
b = "python"
if "on" in a and "on" in b:
    print(True)
else:
     (False) 

#length of the text python and convert the value to float and convert it to string
A = "python"
B = "Dragon"
print(len(A))
print(len(B))
print(float(len(A)))
print(float(len(B)))
print(str(float(len(A))))
print(str(float(len(B))))

# divisible & remiander = 0

number = int(input("Enter your number:"))
if number %2 == 0:
     print("Even")
else:
     print("Odd")

#floordivision
h = 7//3
if h == int(2.7):
     print(True)   

# type '10' = type 10
t ='10'
u = 10
if t == u:
     print(True)

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
print (5,1,5,25,)