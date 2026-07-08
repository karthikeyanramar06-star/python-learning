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