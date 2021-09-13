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
Marks = {
    1:77,
    2:76,
    3:65,
    4:78,
    5:62
}
a = type(Marks)
print(a)
