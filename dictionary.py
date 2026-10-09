#create dictionary with student details
students = {
    101:{"Name": "Aditi","Scores":[10,20,35]},
    102:{"Name": "Shreya","Scores":[47,60,50]},
    103:{"Name": "karan","Scores":[0,15,95]},
    104:{"Name": "Priya","Scores":[55,12,43]},
    105:{"Name": "Sujal","Scores":[49,20,36,47]},
}

#calculate avg score and flag pass/fail
for sid,details in students.items():
    avg = sum(details["Scores"])/len(details["Scores"])
    details["Average"]=avg
    details["Passed"]=avg >=30 #boollean flag

#print names of students who passed
print('Students who passed')
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])
