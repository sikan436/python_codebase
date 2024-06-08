class Student:
    def __init__(self,name,house):
        
        self.name=name
        self.house=house
    
    def __str__(self):
        return f"{self.name} stays in {self.house}"
    
    @classmethod
    def get(cls):
        name=input("name")
        house=input("house")
        return cls(name,house)


    

def main():
    student=Student.get()
    print(student)



if (__name__)=="__main__":
    main()

