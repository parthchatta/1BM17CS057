class calldetail:
    def __init__(self,a,b,c,d):
        self.calledby=a
        self.calledto=b
        self.duration=c
        self.typecall=d

    def display_details(self):
        print("caller phone no. :",self.calledby)
        print("reciever phone no. :",self.calledto)
        print("duration :",self.duration)
        print("call type :",self.typecall)

class util:
    def __init__(self):
        self.list_call_objects=None
    def parse_customer(self,list_str):
        call_detail= []
        for i in range(len(list_str)):
            lis=list_str[i].split(',')
            call_detail.append(calldetail(lis[0],lis[1],lis[2],lis[3]))
            call_detail[i].display_details()
            print()

call='996264589,9595954136,23,STD'
call2='1646565165,687641361,45,local'
call3='4968446864,486454599,8,ISD'

list_str=[call,call2,call3]
util().parse_customer(list_str)

            
            
        
