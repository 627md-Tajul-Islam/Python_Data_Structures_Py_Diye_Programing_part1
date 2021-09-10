li = [1,2,3,4]
new_li = []
for x in li:
    new_li.append(2 * x) # everyone is double to their previous books
print(new_li)

# using list comprehension
new_li = [2* x for x in li ]
print(new_li)

li = [1,2,3,4,5,6,7,8,9,10]
even_number = []
for x in li:
    if x % 2 == 0:
        even_number.append(x)
print(even_number) # without list comprehension

even_number = [x for x in range(1,11) if x %2 ==0]
print(even_number)
