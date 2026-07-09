#find and rfind
text = "Python is fun because Python is powerful because Python is easy."
print(text.find("because"))
print(text.rfind("because"))
#strip
language =  "        Python Programming        "
print(language.strip(" "))
#join
fruits = ["Apple", "Banana", "Orange", "Mango"]
print("|".join(fruits))
#str format
name = "Karthi"
course = "Python"
score = 95.4567
print("%s is learning %s and scored is %.2f%%"%(name,course,score))       
print("Name\tAge\tCity\nKarthi\t20\tChennai\n\nPython is awesome")
#len
text = "Python Programming"
print(len(text))
#slicing
text = "Programming"
print(text[3:7])
#reverse a string
text = "Python"
print(text[::-1])
#lowercase
sentence = "Python Is Awesome"
print(sentence.lower())
sentence = "I love Java"
print(sentence.replace("Java","Python"))
#split
sentence = "apple,banana,mango,orange"
print(sentence.split(","))
#join
languages = ["Python", "Java", "C++", "JavaScript"]
print("->".join(languages))
#formatting
name = "Karthi"
age = 20
cgpa = 8.9876
print( "%s is %d years old and has a cgpa of %.2f "%(name,age,cgpa))
print("Course\tDuration\tFee\nPython\t30 Days \tFree\n\nLet's Learn Python!")
#find and slice
sentence = "You cannot end a sentence with because because because is a conjunction"
start=sentence.find("because")
end= start + len("because because because")
print(sentence[start:end])