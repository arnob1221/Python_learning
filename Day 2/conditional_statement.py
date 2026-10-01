#check for vote age
# age = 16

# if(age >= 18): #print(true) ata likhle condition ar check korto na, always true return korto.
#     print("Able to cast vote to the BD govt.")
# else:
#     print("Aren't able to cast vote.")

#traffic light check

# light = input("Enter the current traffic status: ")
# print("Current Light Status: ", light)
# if(light == "green" or light == "Green"):
#     print("Go!") # print er age 4 ta space ba 1 ta tabs etake indentation bole

# elif(light == "red"):
#     print("Stop!")

# elif(light == "yellow"):
#     print("Stop here please!")

# else:
#     print("Light is broken budddy!")

#varsity grade point check

# marks = int(input("Enter your marks: "))
# if(marks >= 80):
#     print("A+, well done!")
# elif(marks >= 75):
#     print("A, Good!")
# elif(marks >= 70):
#     print("A-, More study needed!")
# elif(marks >= 65):
#     print("B+, More study needed!")
# elif(marks >= 60):
#     print("B+, Improve needed!")
# elif(marks >= 55):
#     print("B-, Do study harder!")
# elif(marks >= 50):
#     print("C+, Very bad!")
# elif(marks >= 45):
#     prnt("C, Bad!")
# else:
#     print("Fail, Better luck next time!")

# marks = int(input("Enters mark:"))
# if(marks >= 90):
#     grade = "A +" #avabei print kora jabe
# print("Grade is", grade)

#nesting theory
# age = int(input("Enter your valid age :"))
# if(age >= 18):
#     if(age >= 85):
#         print("Cant not drive because of overage!")
#     else:
#         print("Can drive.")
# else:
#     print("Can not drive because of underage.")


age = int(input("Enter age:"))
if(age >= 18):
    if(age >= 85):
        print("cant")
    else:
        print("Can")
else:
    print("underage")
