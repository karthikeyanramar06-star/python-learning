#concatination
word_1 = "Thirty "
word_2 = "Days "
word_3 = "of "
word_4 = "Python "

full_sentence = word_1 + word_2 + word_3 + word_4
print(full_sentence)

#concatination 2
first_word = "coding"
second_word = " for"
third_word = " all"

entire_sentence = first_word + second_word + third_word 
print(entire_sentence)

#assign
company = "coding for all"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.swapcase())
print(company.title())
print(company[7:])
print(company.find("coding"))
print(company.replace("coding" , "Python"))
company_2 = "Python For Everyone"
print(company_2.replace("Everyone" , "all" ))
print(company.split(" "))
company_3 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company_3.split(","))
print(company[0])
print(len(company) -1)
print(company[10])
print(company_2[0] + company_2[7] + company_2[11])
print(company[0]+company[7]+company[11])
print(company.index("c"))
print(company.index("f"))
company_4 = "Coding For All People"
print(company_4.rfind("l"))
sentence_1 = "You cannot end a sentence with because because because is a conjunction"
print(sentence_1.find("because"))
print(sentence_1.rindex("because"))
#slicimg
start = sentence_1.find("because")
print(start)
length = len("because,because,because")
end = start + length
print(end)
print(sentence_1[start:end])
print(sentence_1[31:53])
#starswith
if company.startswith("coding"):
    print("yes")
else : 
    print("no")
#endswith
if company.endswith("coding"):
    print("yes")
else : 
    print("no")

#remove spaces
company_5 = "  Coding For All      "
print(company_5.strip(" "))
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
world_1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(world_1))
print('''I am enjoying this challenge.\nI just wonder what is next.''')
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = "The area of a circle with radius %d is %.2f meters square." %(radius,area)
print(formated_string)
name = "karthi"
age = 20
mark = 99.9
print("my name is %s ,im %d years old,i scored %.2f"%(name,age,mark))
#string format
a = 8
b = 6

print('{} + {} = {}'.format(a,b,a + b ))
print('{} + {} = {}'.format(a,b,a - b))
print('{}*{}={}'.format(a,b,a*b))
print('{}/{}={}'.format(a,b,a%b))
print('{}%{}={}'.format(a,b,a%b))
print('{}//{}={}'.format(a,b,a//b))
print('{}**{}={}'.format(a,b,a**b))