import random
class Hat:
    houses=["Gryinfindor","huffenpuff","slytherine","ravenclaw"]
    @classmethod
    def sort(cls,name):
        print(name ,"is in" ,  random.choice(cls.houses))


Hat.sort("harry")