from sys import getsizeof

x=10
print(getsizeof(x))
#output:28

y="hello"
print(getsizeof(y))
#output:46

z=3.5
print(getsizeof(z))
#output:24

#Due to internal structure of data type size of memory varies