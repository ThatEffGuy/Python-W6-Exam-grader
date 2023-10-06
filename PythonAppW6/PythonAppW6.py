# Exam Mark Grader
# Craig Ferguson
# 181120

def getValues():
    name = input("Enter the students first name: ")
    surname = input("Enter the students surname: ")
    school = input("Enter the students school: ")
    maxMark = int(input("Please input the maximum mark available: "))
    mark = int(input("Please input the students mark: "))
    percent = round(mark * 100 / maxMark,0)
    return name, surname, school, maxMark, mark, percent
#End get val

def getGrade(percent):
    if percent >=70:
        grade = "A"
    if percent >=60 and percent <70:
        grade = "B"
    if percent >=50 and percent <60:
        grade = "C"
    if percent >=45 and percent <50:
        grade = "D"
    if percent <45:
        grade = "FAIL"
    return grade

#end get grade

def printResult(name, surname, percent, grade):
    print ("-----------------------------")
    print ("SQA Exam Grader")
    print ("Student ",name + " " + surname)
    print ("School", school)
    print ("Percentage ",percent,"%")
    print ("Grade ",grade)
#end results


#Main program

name, surname, school, maxMark, mark, percent = getValues()
grade = getGrade(percent)
printResult(name, surname, percent, grade)