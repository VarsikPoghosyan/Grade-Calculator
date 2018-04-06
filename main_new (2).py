import json

def loadSetupData():
    with open('gc_setup.json') as data_file:
        course = json.load(data_file)

    grades = course["course_setup"]
    return grades

def loadStudentGrades():
    with open('gc_grades.json') as data_file:
        user_grades=json.load(data_file)

    user_grades= user_grades["mygrades"]
    return user_grades

def askForAssignmentMarks(grades, user_grades):
    current_grades = {"mygrades": {}}

    for key in grades:
        print(key)
        change=input("Would you like to change the grade? Type 0 for no and 1 for yes")

        if change!=0 and change!=1:
            change=input("Please put in either 0 for no or 1 for yes.")
        if change==0:
            if ((user_grades[key]>=0) and (user_grades[key]<=100)) or (user_grades[key]==-1):
                current_grades["mygrades"][key]= user_grades[key]
            else:
                change=1
        if change==1:
            update= input("What is your Current Grade for: " + key + " . Please insert -1 if you don't have a grade yet")
            while True:
                if ((update>=0) and (update<=100)) or (update==-1):
                    current_grades["mygrades"][key]= update
                    break
                else:
                    update=input("Please enter a number between 0 and 100. Please insert -1 if you don't have a grade yet")
    return current_grades

def saveGrades(current_grades):
    print (json.dumps(current_grades))
    file = open("gc_grades.json", "w")
    file.write(json.dumps(current_grades))
    file.close()

def printCurrentGrade(grades, current_grades):
    curr_grade = 0.0
    for key in current_grades["mygrades"]:
        if current_grades["mygrades"][key] != -1:
            calc_grade = float(current_grades["mygrades"][key]) * grades[key] / 100
            curr_grade = curr_grade + calc_grade

    print (curr_grade)
    return curr_grade

def printLetterGrade(curr_grade, matrix):
    for i in range(len(matrix)):
        if curr_grade>= matrix[i]["min"] and curr_grade<=matrix[i]["max"]:
            print matrix[i]["mark"]

def main():
    g = loadSetupData()
    grades= g["grade_breakdown"]
    user_grades= loadStudentGrades()
    current_grades = askForAssignmentMarks(grades, user_grades)
    saveGrades(current_grades)
    curr_grade= printCurrentGrade(grades, current_grades)
    conv_matrix= g["conv_matrix"]
    printLetterGrade(curr_grade, conv_matrix)

main()
