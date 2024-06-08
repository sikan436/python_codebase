students=[
    {"name":"Hermoine","Hhouse":"Grifindor","patronous": "Otter"},
    {"name":"Ron","Hhouse":"Grifindor","patronous": "Stag"},
    {"name":"Harry","Hhouse":"Grifindor","patronous": "nanag"},
    {"name":"Draco","Hhouse":"Slythrine","patronous": None},
]

grinfindors=[
         student["name"] for student in students if student["Hhouse"]=="Grifindor"
]

for gryfindor in sorted(grinfindors):
    print("name",gryfindor)