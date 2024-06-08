import csv

students=[]

with open("names.txt") as file:
    reader= csv.reader(file)
    for row in reader:
        students.append({"name":row[0],"house":row[1]})


for student in sorted(students,key=lambda ab:ab["name"]):
    print(f"{student['name']} {student['house']} hai ")

