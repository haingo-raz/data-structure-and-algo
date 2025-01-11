#Print statement
print("Hello World!")

#Conditions
if (5 > 2): 
    print("True")

#Variable assignment
age = int(3)
print(type(age))

# Multiple variables assignment
name, age2 = 'Anna', 12
print('Her name is ', name, ' and she is ', age2)

#Global variable
def calculateAgeInTwentyYears(num):
    global age3
    age3 = 20
    print(num + age3)

calculateAgeInTwentyYears(21)
print(age3)
    

