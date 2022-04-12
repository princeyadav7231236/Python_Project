# Health Management System

def getdata():
    import datetime
    return datetime.datetime.now()


while True:
    name = input("Enter the name : ")
    data = input("Type ( l ) to log and ( r ) to retrieve your data : ")
    data2 = input("Type ( d ) to log the diet plan or ( e ) to log exercise : ")

    if (name == "Hammad" or name == "hammad") and (data == "l" or data == "log") and (data2 == "d" or data2 == "diet plan"):
        h = open("Hammad_diet_plan.txt", "a")
        a = input("Enter your  diet plan : \n")
        h.write(a)
        h.write("\n")
        print("Successfully entered your diet plan  ")
        print("Type ( c ) to continue or ( e ) to exit : ")
        i = input()
        h.close()
        if i == "c":
            continue
        elif i == "e":
            break
        else:
            print("You didn't gave an appropriate input ")
            break

    elif (name == "Hammad" or name == "hammad") and (data == "r" or data == "retrieve") and (data2 == "d" or data2 == "diet plan"):
        file1 = open("Hammad_diet_plan.txt")
        print(getdata(), file1.readlines())
        file1.close()
        break

    elif (name == "Rohan" or name == "rohan") and (data == "l" or data == "log") and (data2 == "d" or data2 == "diet plan"):
        h = open("Rohan_diet_plan.txt", "a")
        a = input("Enter your  diet plan : \n")
        h.write(a)
        h.write("\n")
        print("Successfully entered your diet plan  ")
        print("Type ( c ) to continue or ( e ) to exit : ")
        i = input()
        h.close()
        if i == "c":
            continue
        elif i == "e":
            break
        else:
            print("You didn't give an appropriate input ")
            break

    elif (name == "Rohan" or name == "rohan") and (data == "r" or data == "retrieve") and (data2 == "d" or data2 == "diet plan"):
        file1 = open("Rohan_diet_plan.txt")
        print(getdata(), file1.readlines())
        file1.close()
        break

    elif (name == "Harry" or name == "harry") and (data == "l" or data == "log") and (data2 == "d" or data2 == "diet plan"):
        h = open("Harry_diet_plan.txt", "a")
        a = input("Enter your  diet plan : \n")
        h.write(a)
        h.write("\n")
        print("Successfully entered your diet plan  ")
        print("Type ( c ) to continue or ( e ) to exit : ")
        i = input()
        h.close()
        if i == "c":
            continue
        elif i == "e":
            break
        else:
            print("You didn't give an appropriate input ")
            break

    elif (name == "Harry" or name == "harry") and (data == "r" or data == "retrieve") and (data2 == "d" or data2 == "diet plan"):
        file1 = open("Harry_diet_plan.txt")
        print(getdata(), file1.readlines())
        file1.close()
        break

    elif (name == "Rohan" or name == "rohan") and (data == "l" or data == "log") and (data2 == "e" or data2 == "Exercise"):
        h = open("Rohan_Exercise_plan.txt", "a")
        a = input("Enter your  Exercise plan : \n")
        h.write(a)
        h.write("\n")
        print("Successfully entered your Exercise plan  ")
        print("Type ( c ) to continue or ( e ) to exit : ")
        i = input()
        h.close()
        if i == "c":
            continue
        elif i == "e":
            break
        else:
            print("You didn't give an appropriate input ")
            break

    elif (name == "Rohan" or name == "rohan") and (data == "r" or data == "retrieve") and (data2 == "e" or data2 == "Exercise"):
        file1 = open("Rohan_Exercise_plan.txt")
        print(getdata(), file1.readlines())
        file1.close()
        break

    elif (name == "Harry" or name == "harry") and (data == "l" or data == "log") and (data2 == "e" or data2 == "Exercise"):
        h = open("Harry_Exercise_plan", "a")
        a = input("Enter your  Exercise plan : \n")
        h.write(a)
        h.write("\n")
        print("Successfully entered your Exercise plan  ")
        print("Type ( c ) to continue or ( e ) to exit : ")
        i = input()
        h.close()
        if i == "c":
            continue
        elif i == "e":
            break
        else:
            print("You didn't give an appropriate input ")
            break

    elif (name == "Harry" or name == "harry") and (data == "r" or data == "retrieve") and (data2 == "e" or data2 == "Exercise"):
        file1 = open("Harry_Exercise_plan")
        print(getdata(), file1.readlines())
        file1.close()
        break

    elif (name == "Hammad" or name == "hammad") and (data == "l" or data == "log") and (data2 == "e" or data2 == "Exercise"):
        h = open("Hammad_Exercise_plan", "a")
        a = input("Enter your  Exercise plan : \n")
        h.write(a)
        h.write("\n")
        print("Successfully entered your Exercise plan  ")
        print("Type ( c ) to continue or ( e ) to exit : ")
        i = input()
        h.close()
        if i == "c":
            continue
        elif i == "e":
            break
        else:
            print("You didn't give an appropriate input ")
            break

    elif (name == "Hammad" or name == "hammad") and (data == "r" or data == "retrieve") and (data2 == "e" or data2 == "Exercise"):
        file1 = open("Hammad_Exercise_plan")
        print(getdata(), file1.readlines())
        file1.close()
        break
