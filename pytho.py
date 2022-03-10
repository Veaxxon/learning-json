import json
file = open('students.json')
data = json.load(file)
male = 0
female = 0
male_grades= 0
male_age= 0
female_age =0
female_grades =0

for student in data["Students"]:
    if student['Gender'] == 'Female':
        female += 1
        female_grades += int(student['Grade'])
        female_age += int(student['Age'])
    else:
         
        male += 1
        male_grades += int(student['Grade'])
        male_age += int(student['Age'])

print(f"""
Sieviešu vidējā atzīme: {int(female_grades / female)}
     vidējais vecums  : {int(female_age / female)}
Vīriešu vidējā atzīme: {int(male_grades / male)}
     vidējais vecums  : {int(male_age / male)}
""")

    









#UZDEVUMS 2
#Atrodi vidējo studentu atzīmi (Grade), pa vecuma grupām: līdz 20 g., no 20 līdz 29 g un 30+ g.
#Average <20
#Avreage 20-29
#average 30+