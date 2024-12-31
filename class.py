class MyComplexNumber :
    #construtor methods
    def __init__(self,real=0,imag=0):     #self means reference of the object
        print("My Complex Number program executing....")
        self.real_part = real
        self.imag_part = imag
    
    def displayComplex(self):
        print("{0}+{1}j". format(self.real_part,self.imag_part))


#Create an new object against MyComplexNumber class
complex1 = MyComplexNumber(40,50)
complex1.displayComplex()