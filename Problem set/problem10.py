# Write a program to detect double space in a string.
str1="Akash is a good  boy"
print(str1.find("  "))  # Find method use to find the index number of anyone
print(str1.find("goo"))  # Find method use to find the index number of anyone


# Replace the double space from problem 3 with single spaces.
print(str1.replace("  "," "))  # Akash is a good boy
print(str1) # Akash is a good  boy , this output same as the input.. isn't interesting.. 
# in Python string is an immutable that's why any changhing in the variable doesn't effect in main part