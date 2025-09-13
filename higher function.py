from functools import reduce
l=[1,2,3,4,5,6,7]
def sum(x,y):
    return x+y
x= reduce(sum,l)
print(x)

    #lambda funtion

    #lambda(parameter):l-expression

  #  x=lambda x,y : print(x+4)
   # print(x(4,5))

from functools import reduce
l=[1,2,3,4,5,6,7]
x=list(map(lambda x: x**2,l))
print(x)

x=list(filter(lambda x: x if x>2 else None,l))
print(x)