bd_division_info = {}

# 1
bd_division_info["Barisal"] = {
    "district": 6,
    "upzilla": 39,
    "union":333
}
#2
bd_division_info["Khulna"] = {
    "district": 10,
    "upzilla": 59,
    "union":270
}
#3
bd_division_info["Dhaka"] = {
    "district": 10,
    "upzilla": 59,
    "union":1833
}
print(bd_division_info)

# just name using key method
divisions = bd_division_info.keys()
print(divisions)

# loop on keys

for division in divisions:
    print("#",division)

# key and value
for key in bd_division_info:
    print(key)
    print(bd_division_info[key])

# 2nd way
for key, value in bd_division_info.items():
    print(key)
    print(value)
