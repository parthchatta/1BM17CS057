def even(li):
    l=[]
    for a in li:
        if a%2==0:
            l.append(a)
    for i in l:
        print(i,end=" ");

n=int(input("enter number of elements: "))
li=[]
for i in range(n):
    a=int(input())
    li.append(a)

even(li)
