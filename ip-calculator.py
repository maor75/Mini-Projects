def ip_to_list(ip_address):
    ip_list = list(ip_address.split("."))
    list2 = []
    for i in ip_list:
        res = int(i)
        list1 = []
        while res != 0:
         if res %2 == 0:
            list1.append(0)
            res //= 2
         else:
           list1.append(1)
           res //= 2
        while len(list1) < 8 :
         list1.append(0)
        list2.append(list1.join[::-1])
    print(list2) 
if __name__ == "__main__":
   ip_to_list("11.12.13.14")
   
