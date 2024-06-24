class Vechicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def Move(self):
        print("Vechicle Move")
        
    
class Car(Vechicle):
    pass

class Aeroplane(Vechicle):
    def __init__(self,brand,model):
        super().__init__(brand,model)
        
    def Move(self):
        print("Aeroplane Fly")
        

class Boat(Vechicle):
    def __init__(self,brand,model):
        super().__init__(brand,model)
        
    def Move(self):
        print("Boat Sail")
            

car=Car("BMW","X5")
aeroplane=Aeroplane("Boeing","747")
boat=Boat("Boeing","747")

# print the move
car.Move()
aeroplane.Move()
boat.Move()