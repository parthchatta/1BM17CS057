n=int(input("enter the number"))
li=[0,1]
for i in range(2,n):
    li.append(li[i-1]+li[i-2])
for k in li:
    print(k,end=" ")
