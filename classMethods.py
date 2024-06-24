class Hunk:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        
    def __str__(self):
        return f"My name is {self.name} and my address is {self.address}"

    def setName(self,name):
        self.name=name
    
    def getName(self):
        return self.name
    
    @staticmethod
    def hello():
        print("Hello World from the static methods")
    
    @classmethod
    def classMethods(cls):
        print("Hello World from the class methods")

hunk=Hunk("sahadev","kathmandu")
Hunk.classMethods()
Hunk.hello()
hunk.setName("dahit")
print(hunk.name)