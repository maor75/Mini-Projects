bin = input("give your bin: ")
result =  0
power = 0 
for i in bin[::-1]:
    result += (int(i) * (2 ** power))
    power += 1
print(result)
