students= [
    {"name": "hermoine","house": "grifindor"},
    {"name": "harry","house": "grifindor"},
    {"name": "ron","house": "grifindor"},
    {"name": "draco","house": "ravenclaw"}
]
houses=set()

for student in students:
    
        houses.add(student["house"])

for house in sorted(houses):
    print(house)

print(set())