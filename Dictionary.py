"""
# this was for 1 number
Marks = [80,90,67,84,65]
Roll = input("Please enter your roll number: ")
print("Your mark is", Marks[int(Roll)-1])

# this is for double subject
Mark = [[90,60],[80,70],[50,50],[70,50],[40,60]]
Rolls = input("Please enter your roll number: ")
print("Your mark of English & Bangla is :", Mark[int(Rolls)-1])
"""

# dictionary

# maintained sequence
Marks = {
    1:77,
    2:76,
    3:65,
    5:62,
    4:78
}
a = type(Marks)
print(a)
b = Marks[4]
print(b)

# does not maintain maintained sequence

Marks = {
   500: 90,
   200: 80,
   100: 70,
   400: 50,
   300: 60,
}
b = Marks[400]
print(b)

# does not matter if its not a number
Marks = {
    "A1": 90,
    "B2": 60,
    "C3": 80,
    "D4": 50,
    "E5": 30,
}
b = Marks["A1"]
print(b)

dic = {}
print(dic)
a = type(dic)
print(a)

dic[1] = "one" # inserting a value
print(dic)

dic[2] = "two" # inserting a value
print(dic)

dic = {
    "a": "A",
    "b": "B",
    "c": "C"
}
#a=dic["e"] it will produce an error

# tuple can be inserted
dt = {
    "a":"A",
    "b":"B",
    "c":"C",
}
dt[(1,2,3)] = "tuple"
print(dt)

# list can not be added
li = [1,2,3]
#dt[li] = "list"
#print[dt]

# set can not be added
set = {1,2,3}
#dt[set] = "set"
#print((dt))

# marks of dual sub
marks = {
    "one101" : {"Bangla":74,"English":73},
    "two102" : {"Bangla":70,"English":83},
    "three103" : {"Bangla":54,"English":63},
}
print(marks)
print(marks["one101"]) # default numbers
print(marks["two102"]["English"]) # specific number

marks["three103"] = {"Bangla":74,"English":93} # updating
print(marks)