#Static Method
'''
If we use Static Method we don't need to use (self) Parameter
'''



class MathOperation :
    @staticmethod
    def add(x, y):
        return(x+y)

maths = MathOperation.add(5, 8)
print("Result:", maths)    
