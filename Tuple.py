x = (1,2,3)
print(x)
a=type(x)
print(a)

x = 1
a = type(x)
print(a)

x = 1,
a = type(x)
print(a)

t = ()
b = type(t)
print(b)
print(t)

tpl = (1,2,3,4,5)
a = tpl[0]
print(a)

li = [1,2,3,4,5]
print(li)
li[0] = 100
print(li) # lists can change

tuple = (1,2,3,4,5)
print(tuple)
#tuple[0] = 100 tuple cant change
#print(tuple) 'tuple' object does not support item assignment

nums = (1,2,3,4)
n1,n2,n3,n4 = nums
print(n1) # we can pack it
# we can print it individually
t = n1,n2
print(t) # we can also unpack it