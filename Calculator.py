import csv
import pandas as pd
rows=[]
with open ('Data3.csv','r') as f:
  csv_reader = csv.reader(f)
  for row in csv_reader:
    rows.append(row)
Data = rows[1:]    
new_planet_data = []
for a in Data:
  
  if a == []:
    continue
  else:
    if a[8]== 'Unknown':
     continue
    if a[7]=='Unknown':
     continue
  
  new_planet_data.append(a)
  
print(len(new_planet_data))    

print(Data[1])

star_mass = []
star_radius = []
star_name=[]

for j in new_planet_data:
  
  if j == []:
    continue
  else:
    if j[8]== 'Unknown':
     continue
    if j[7]=='Unknown':
     continue
  
  #if a == []:
   # continue

  radius_value = j[8]
  star_radius.append(radius_value)
  mass_value = j[7]
  star_mass.append(mass_value)
  star_name.append(j[1])
    
print(j[8][2])
star_gravity = []
for index, name in enumerate(star_name):
    gravity = float(star_mass[index])*6.957e+8/((float(star_radius[index]))*1.989e+30)**2
    star_gravity.append(gravity)

