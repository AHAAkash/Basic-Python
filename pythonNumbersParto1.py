#Python have 3 data type - Integer, Float, Complex number .
value1=100
print(type(value1))
print(isinstance(value1,int))  #isinstance() is a boolean function that return true or false to check value 
print(isinstance(value1,float)) #is int,float,complex
print(isinstance(value1,complex))
# <class 'int'>
# True
# False
# False

value2=101.11
print(type(value2))
print(isinstance(value2,int))
print(isinstance(value2,float))
print(isinstance(value2,complex))
# <class 'float'>
# False
# True
# False

value3= 50+6J
print(type(value3))
print(isinstance(value3,int))
print(isinstance(value3,float))
print(isinstance(value3,complex))
# <class 'complex'>
# False
# False
# True

#TypeCasting
print(int(101.11))
print(int(-20.78))
print(float(20.22))
# 101
# -20
# 20.22

