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
    A: 90,
    B: 80,
    C: 70,
    D: 50,
    E: 60,
}