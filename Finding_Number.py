l = (1,4,9,16,25,36,49,64,81,100)
n = int(input("enter number : "))
idx = 0
while idx < len(l) :
    if(l[idx] == n) :
     print("Found at idx : " , idx)
    idx += 1      