list = [1,2,3,4,5,6,8,2,5]
cnt = {}
for element in list:
    if element not in cnt.keys():
        print("Found New Element")
        cnt[element] = 1
    else:
        cnt[element] += 1