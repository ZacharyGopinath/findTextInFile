# works for mac os

import os

# target = input('word: ')
target = ''
locations = []

directory = os.fsencode(DIRECTORY_AS_STRING)
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".c"):  # change depending on filetype(s)
        locations.append(filename)

        continue
     else:
         continue

for i in range(len(locations)):
    file = locations[i]
    with open(DIRECTORY_AS_STRING + '/'  + file, "r") as file:
        for line_number, line in enumerate(file, start=1):  
            if target in line:
                print(f"target '{target}' found in {locations[i]} on line {line_number}")
