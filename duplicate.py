lst = [1, 2, 3, 4, 5, 2, 3]
hashset = set()

for num in lst:
    if num in hashset:
        print(True)
        break
    else:
        hashset.add(num)
else:
    print(False)
