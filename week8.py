file1 = open("file1.txt")
#read = file1.read(5)
#read2 = file1.readline()

file2 = open('file2.csv','w')
file2.write("Name,Grade")
file2.writelines(['Mac,D\n','Ben,C\n','Alex,C\n'])

#File2.Close()

file3 = open('file2.csv','a')
file3.write('Brodie,F\n')

grades = ["A","B","C","D","F"]
students = ["Mac","Ben","Alex","Farhad","Sebatian","Kaylee","Josh","Sam","Brodie","Skyler","Kate"]

import random
with open("Grades.csv",'w') as f:
    f.write('Name,Grade\n')
    for student in students:
        rand = random.randint(0,len(grades)-1)
        print(student,grades[rand])
        f.writelines('{student},{grades[rand]}\n')

















dummy_variable = 0