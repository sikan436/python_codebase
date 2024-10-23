class vehicle:

    def __init__(self,type):
        self.type=type

class Toyotacar(vehicle):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
car1=Toyotacar('nai gadi','diesle')

print(car1.type)
