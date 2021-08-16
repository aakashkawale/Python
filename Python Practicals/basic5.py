#using sys module to get size of varible
import sys

a=10
b=1.2
c='abc'
x=sys.getsizeof(a) 
print(x)
x=sys.getsizeof(b)
print(x)
x=sys.getsizeof(c)
print(x)