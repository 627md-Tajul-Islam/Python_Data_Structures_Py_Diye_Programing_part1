saarc = ["Bangladesh", "India", "Srilanka","Bhutan", "Pakistan", "Nepal"]
print(saarc)
saarc.append("Afghanistan")
print(saarc) # append method to put something

saarc.sort()
print(saarc)  # ranked from 1st to last

list = [1,3,5,5,6,4,3,1]
list.sort()
print(list) # ranked from 1st to last

# off topic
a=[1,2,3,4,5]
b=a+[6,7,8,9,10]
print(b) # adding 2 lists

list = [10,34,35,43,56456,456,35,3,2354,23]
list.reverse()
print(list) # ranked from last to fast

li = ["mango","banana","orange"]
li.reverse()
print(li) # reversd

li = ["mango","banana","orange"]
li.insert(0,"apple") # adds in the 1st index, need 2 arguements
print(li)

li = ["mango","banana","orange"]
li.insert(2,"apple") # we can mention the index number so that the index can take place
print(li)

# insert(index,item)

friends = ["Rakib","alve","tuhin","likhon","sabit"]
friends.remove("tuhin")
print(friends) # removes an element

""" 
friends = ["Rakib","alve","tuhin","likhon","sabit"]
friends.remove("tajul")
"""  # it will throw an error cause the element is not in the list
""" 
friends = ["Rakib","alve","tuhin","likhon","sabit"]
name = "Rakib"
if name in friends:
    remove(name)
else:
    print(name, "Not in list")
"""

friends = ["Rakib","alve","tuhin","likhon","sabit"]
item = friends.pop()
print(item)
print(friends) # returns only the last element and clears the same element from the list

friends = ["Rakib","alve","tuhin","likhon","sabit"]
item = friends.pop(1) # we can also set the index number
print(item)
print(friends)

a=[1,2,3,4,5]
b=[6,7,8,9,10]
a.extend(b) # we can add list using extend methods
print(a)

li = [1,1,2,3,4,5,6,7,7,8,]
a = li.count(7)
print(a) # counts the element

li = [1,1,2,3,4,5,6,7,7,8,]
del(li[1])
print(li) # delete function

li = []
for x in range(10):
    li.append(x)
print(li) # empty list

