#Python Decimal
data1 = 0.1+0.2
print(data1)
# 0.30000000000000004 this is the output. But in mathematics term we just get 0.3 only. Here we get this for 
#hardware issue, that's provides us garbage value. to overcome from this we use following process:
from decimal import Decimal as d
print(d('0.1')+d('0.2'))
print(d('1.2')+d('1.3'))
# 0.3
# 2.5

#Python Fractions
from fractions import Fraction as f
print(f(1.5))
print(f(5))
print(f(1,5))
# 3/2
# 5
# 1/5

#python math module
import math
print(math.pow(2,4)) # 16.0
print(math.pi)
print(math.log(10))
print(math.exp(24))
print(math.factorial(34))
# 3.141592653589793
# 2.302585092994046
# 26489122129.84347
# 295232799039604140847618609643520000000

#Python Random Variable
import random
print("Printing Random Variable:", random.randrange(41,200))
# Printing Random Variable: 134

print(random.random()) # 0.3415532277015423

day=['sun','Mon','Thu','Wed','Tue','Fri','Sat']
print(random.choice(day))  # Thu
print(day)  #['sun', 'Mon', 'Thu', 'Wed', 'Tue', 'Fri', 'Sat']
random.shuffle(day)
print(day) # ['Thu', 'Fri', 'Mon', 'Tue', 'Wed', 'Sat', 'sun']