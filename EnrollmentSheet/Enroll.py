import json
file_path = 'DataCleaning./EnrollmentSheet./student-enrollment-data.json'
output_path = 'DataCleaning./EnrollmentSheet./courses-output.json'
output_path2 = 'DataCleaning./EnrollmentSheet./class-lists.json'

with open(file_path, 'r') as f:
    student_data = json.load(f)
    
courses = {} 
for i in range (len(student_data)):
    for x in student_data[i]["enlistment"]:
        if x["course code"] not in courses: courses[x["course code"]],courses[x["course code"]]["sections"]  = {},[]
        if x["section"] not in courses[x["course code"]]["sections"] :courses[x["course code"]]["sections"].append(x["section"])
for cc in courses: courses[cc]["sections"].sort() 

class_list = {}
for i,v in courses.items():
    if i not in class_list: class_list[i] = []
    for item in v["sections"]: class_list[i].append({"section" : item, "class list" : []})

for i in range(len(student_data)):
    id = student_data[i]["id"] 
    for x in student_data[i]["enlistment"]:
        coursecode,section = x["course code"] ,x["section"] 
        for y in class_list[coursecode]:
            if y["section"] == section: y["class list"].append(id)
            
for classes in class_list: 
    for lst in class_list[classes]:
        lst["class list"].sort()

with open(output_path, 'w') as f:
    json.dump(courses, f,indent=4)

with open(output_path2, 'w') as f:
    json.dump(class_list, f,indent=4)
