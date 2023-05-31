



# ## Example_1

class Book:
    def __init__(self,n,p,a):
        self.name=n
        self.price=p
        self.author=a
    def __str__(self):
        return self.name
    def __add__(self,second):
        return self.price + second.price
    def __sub__(self,second):
        return self.price - second.price
    def __mul__(self,intvalue):
        return self.price *intvalue
    def __truediv__(self,intvalue):
        return self.price / intvalue

python=Book('Python',1000,'Van Guido Rossom')
django=Book('Django',5000,'ABCD')

print(python+django)
print(python-django)
print(django-python)
print(python*3)
print(django/2)
##print(python.__add__(django))
##print(int(5).__add__(int(5)))









## Example-2
#$ 1st Type

class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def __gt__(self,second):
        a1=self.length*self.breadth
        a2=second.length*second.breadth
        return True if a1>a2 else False
r1=Rectangle(234,100)
r2=Rectangle(234,102)
print(r1>r2)






#$ 2nd Type

class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def area(self):
        return self.length * self.breadth

    def __gt__(self,second):
        if self.area() > second.area():
            return True
        else:
            return False
r1=Rectangle(234,100)
r2=Rectangle(234,102)
print(r1>r2)

