import json
import os

if not os.path.exists("C:/project"):
    os.mkdir("C:/project")
else:
    print("myfolder already exist")
while 1:
    accountType = int(input("select:\n1-professor\n2-student\n3-0 to stop\n "))
    operation = int(input("1-sign up \n2-log in "))
    if accountType == 1:
        if operation == 1:
            professorInfo = []
            # prefessor sign
            print("Enter[id,name,email,password]")
            for i in range(0, 4):
                professorInfo.append(input())
            if os.path.exists("professor" + professorInfo[1]):
                file = open("C:/project/professor " + professorInfo[1], "a")

            else:
                file = open("C:/project/professor " + professorInfo[1], "a")
                jsonData = {
                    "id": professorInfo[0],
                    "name": professorInfo[1],
                    "email": professorInfo[2],
                    "password": professorInfo[3],
                }
            file.write(json.dumps(jsonData))

            file.close()

        elif operation == 2:
            # professor login
            for i in range(0, 3):
                name = input("Enter your name: ")
                if not os.path.exists(str("C:/project/professor " + name)):
                    print("not found\n try again")
                    continue
                if os.path.exists(str("C:/project/professor " + name)):
                    file = open("C:/project/professor " + name)
                    data = json.loads(file.read())

                email = input("Enter your email: ")
                password = input("enter your password: ")
                # check email (user[1]) and password (user[2]) for each user
                if data["email"] != email or data["password"] != password:
                    print("invalied email or password")
                    continue
                elif data["email"] == email and data["password"] == password:
                    break
                file.close()

        quiz_title = input("title: ")
        s = int(
            input(
                " 1-add quiz\n 2-remove quiz\n 3-add model answers\n 4-remove model answers\n 5-correction of answers"
            )
        )
        match s:
            case 1:  # add quiz
                while 1:
                    QuestionId = int(input("0 to stop\nEnter Question Id : "))
                    if QuestionId <= 0:
                        break
                    if QuestionId > 0:
                        print("please Add your quiz: ")
                        quiz = open("C:/project/quiz" + quiz_title, "a")
                        quiz.write(str(QuestionId))
                        quiz.write("\n")
                        num = int(input("Add number of questions:"))
                        count = 1
                        while count <= num:
                            quiz.write(input())
                            quiz.write("\n")
                            count += 1
                        quiz.write("\n")
                        quiz.close()
                continue

            case 2:
                os.remove("C:/project/quiz" + quiz_title)
                continue
            case 3:
                numModelAnswer = int(input("Add number of model Answers:"))
                print("please Add your model Answers: ")
                answerFile = open("C:/project/model Answers" + quiz_title, "a")
                count = 1
                while count <= numModelAnswer:
                    answerFile.write(input())
                    answerFile.write("\n")
                    count += 1
                break

            case 4:
                os.remove("C:/project/model Answers" + quiz_title)
                continue
            case 5:  # correction of answer
                while 1:
                    negative = int(input("Enter Negative Number to Stop: "))
                    if negative < 0:
                        break
                    listOfAnswerFiles = os.listdir("C:/project")
                    listOfAnswers = []

                    for file in listOfAnswerFiles:
                        if file.__contains__("answer") == True:
                            listOfAnswers.append(file)

                    print(listOfAnswers)
                    fileIndex = int(input()) - 1
                    fileName = listOfAnswers[fileIndex]
                    jsonData = json.loads(open("C:/project/" + fileName).read())
                    print(jsonData)
                    jsonData["Name"]

                    if os.path.exists("C:/project/student " + jsonData["Name"]):
                        fileOpened = open(
                            "C:/project/student " + jsonData["Name"], "r+"
                        )
                        studentData = json.loads(fileOpened.read())
                        grade = int(input())
                        studentData.update({f"{quiz_title} grade": grade})
                        fileOpened.truncate(0)
                        fileOpened.close()
                        fileOpened = open("C:/project/student " + jsonData["Name"], "w")
                        fileOpened.write(json.dumps(studentData))
                        fileOpened.close()

    elif accountType == 2:
        if operation == 1:
            studentInfo = []
            print("Enter[id,name,email,password,level,age]")
            for i in range(0, 6):
                studentInfo.append(input())
            if os.path.exists("student" + studentInfo[1]):
                file2 = open("C:/project/student " + studentInfo[1], "a")

            else:
                file2 = open("C:/project/student " + studentInfo[1], "a")
                jsonData2 = {
                    "id": studentInfo[0],
                    "name": studentInfo[1],
                    "email": studentInfo[2],
                    "password": studentInfo[3],
                    "level": studentInfo[4],
                    "age": studentInfo[5],
                }
                file2.write(json.dumps(jsonData2))

            file2.close()

            student_name = studentInfo[1]
        elif operation == 2:
            for i in range(0, 3):
                student_name = input("Enter your name: ")
                if not os.path.exists(str("C:/project/student " + student_name)):
                    print("not found\n try again")
                    continue
                else:
                    file2 = open("C:/project/student " + student_name)
                    data2 = json.loads(file2.read())

                email = input("Enter your email: ")
                password = input("enter your password: ")
                if data2["email"] != email or data2["password"] != password:
                    print("invalied email or password")
                    continue
                else:
                    break
            file2 = open("C:/project/student " + student_name, "r")
            print(file2.read())

        listOfQuiz = []
        listOfFiles = os.listdir("C:/project")
        for item in listOfFiles:
            if (
                item.__contains__("quiz") == True
                and item.__contains__("answer ") == False
            ):  # listOfFiles[counter]
                listOfQuiz.append(item)

        print(listOfQuiz)
        fileIndex2 = int(input()) - 1
        file_name = listOfQuiz[fileIndex2]
        fileToOpen2 = open("C:/project/" + file_name)
        print(fileToOpen2.read())

        # answering quiz
        if not os.path.exists("answer " + listOfQuiz[fileIndex2] + " " + student_name):
            answersFile = open(
                "C:/project/answer " + listOfQuiz[fileIndex2] + " " + student_name, "a"
            )

        jsonData = {"Name": student_name}
        numberOfAnswers = int(input("Add number of Answers:"))

        i = 1
        while i <= numberOfAnswers:
            jsonData.update({f"Answer {i}": input()})
            i += 1

        answersFile.write(json.dumps(jsonData))
        answersFile.close()
        continue

    elif accountType == 0 and operation == 0:
        break
