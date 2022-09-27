class Complex:

    def __init__(self,x,y):
        self.r = x
        self.i = y
    
    def display(self):
        return(f'{self.r}+i{self.i}')

    def addition(self, t):
        a = self.r + t.getrealno()
        b = self.i + t.getimgno()
        return(f'{a}+i{b}')

    def getrealno(self):
        return self.r
    
    def getimgno(self):
        return self.i
    
    def setrealno(self, k):
        self.r = k
        print("real number has been set")
        return(self.r)
    
    def setimgno(self, l):
        self.i = l
        print("imaginary number has been set")
        return(self.i)

def addition(x, y):
    m = x.getrealno() + y.getrealno()
    n = x.getimgno() + y.getimgno()
    return Complex(m,n).display()

if __name__ == "__main__":
    obj1 =  Complex(3,4)
    print(obj1.display())
    obj2 = Complex(2,0)
    print(obj2.display())
    print(obj1.addition(obj2))
    print(addition(obj1, obj2))
