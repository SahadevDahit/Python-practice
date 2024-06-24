class MyClass:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    
    def __str__(self) -> str:
        return f"My name is {self.name} and my phone number is {self.phone}"
    
    def display(self):
        print("Hello World "+self.name)
    
    
class childClass(MyClass):
    def __init__(self,name,phone,pkdon):
        super().__init__(name,phone)
        self.pkdon=pkdon
        
        
    def __str__(self) -> str:
        return f"My name is {self.name} and my phone number is {self.phone} and the don name is {self.pkdon}"
       



myObj=childClass("sahadev","1234567890","Donnie")
print(f"My name is {myObj.name} and my phone number is {myObj.phone} and the don name is {myObj.pkdon}")

