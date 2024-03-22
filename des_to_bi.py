num = int(input("give me num: "))
list1 = []
res = num
while res != 0:
 if res %2 == 0:
    list1.append(0)
    res //= 2
 else:
   list1.append(1)
   res //= 2
 

print(list1[::-1])
