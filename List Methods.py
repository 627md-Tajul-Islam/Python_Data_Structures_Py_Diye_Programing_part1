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
# another off
a=[1,2,3,4,5]
b=[6,7,8,9,10]
a.extend(b)
print(a)

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