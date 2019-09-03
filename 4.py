class admission:
    def __init__(self):
        self.id=0
        self.age=0
        self.marks=0
    def validate_marks(self,marks):
        if marks>=0 and marks<=100:
            return True
        else:
            print("enter marks between 0 and 100.")
            return False
    
    def validate_age(self,age):
        if age > 20:
            return True
        else:
            print("age less than 20.")
            return False
    def check_qualification(self,age,marks):
        if self.validate_marks(marks) and self.validate_age(age):
            if marks >= 65:
                return True
            else:
                return False
        else:
            print("marks less than 65.")
            return False
        
    def set_details(self,s_id,age,marks):
        self.id=s_id
        self.age=age
        self.marks=marks
        
    def get_details(self):
        print("id:",self.id)
        print("age:",self.age)
        print("marks:",self.marks)

a=admission()
sid=int(input("enter student id:"))
age=int(input("enter student age:"))
marks=int(input("enter student marks:"))
if a.check_qualification(age,marks):
    a.set_details(sid,age,marks)
    print("hurray u are qualified for admission!")
    a.get_details()
else:
    print("sorry, you are not qualified for admission.")
    
