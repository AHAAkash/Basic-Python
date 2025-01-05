#Many ways to define a string .......
str1="Akash"
str2='Akash'
str3='''Welcome ro my profile'''
print(str1)
print(str2)
print(str3)
str4='''My name is Akash. I am 23 years old. Now   
i trying to learn python for research.'''  #triple quotes String can extrend multiple lines
print(str4)


#Access characters in a string....................
myStr= "Akash"
print(myStr[0:3])  #Start from index 0 all the way till 3 (excluding 3)
print(myStr[1:4])
print(myStr[0])
print(myStr[-4:-1])
print(myStr[0:]) #Same as [0:4]
print(myStr[:5]) #Same as [0:5]


#String are immutable
str1="aaa"
print(str1)
str2="sss"
print(str2)

#Sliding with skip value.....................
word="amazing"
print(word[1:6:2])

#concatanation
str1="Akash"
str2="Hosen"
str3=str1+str2
print(str3)
print(len(str3)) #find string length
print(str1*3) # Same word in multiple time


print(str1.startswith("ka"))
print(str1.startswith("Aka"))
print(str1.endswith("sh"))

