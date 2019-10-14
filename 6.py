def validstring(s):
    a=[]
    d={"(":")","{":"}","[":"]"}
    for i in s:
        if i=="(" or i=="[" or i=="{" :
            a.append(i)
        elif i==")" or i=="]" or i=="}" :
            x=a.pop()
            if d[x]==i:
                pass
            else:
                return False
    if len(a)==0:
        return True
    else:
        return False

s="{{{"
s2="({[)]"
s3="()[]"
print(validstring(s))
print(validstring(s2))
print(validstring(s3))
