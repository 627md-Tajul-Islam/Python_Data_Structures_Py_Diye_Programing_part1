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