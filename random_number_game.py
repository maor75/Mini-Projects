import random 
hidnum = random.randint(1, 100)
usernum = 0 
times = 1 
while usernum != hidnum:
    usernum = int(input("put your gess: "))
    if usernum == hidnum:
     print(f"your correct, the num is {hidnum} and you try {times}")
    elif usernum > hidnum:
     times += 1
     print("your num bigger than the hiden one")
    else:
     times += 1
     print("your num is smaller")
