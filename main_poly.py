#Polymorphism 
'''
When some operater allows to have different meaning according to the context 
'''

     #Operator overloading(Dunder Function)


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumbers(self):
        print(self.real, "i +", self.img, "j")
            
    # Dunder Function
    def __add__(self, num2):
        newReal = self.real + num2.real    
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    def __sub__(self, num2):
        newReal = self.real - num2.real    
        newImg = self.img - num2.img
        return Complex(newReal, newImg)


num1 = Complex(1, 3)
num1.showNumbers()  
num2 = Complex(4, 5)
num2.showNumbers()
num3 = num1 + num2
num3.showNumbers()  
num3 = num1 - num2
num3.showNumbers()  

 

