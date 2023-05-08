print("Hi i am a computure calculator: ")
Random_number_1=""
Random_number_2=""
operator=""
while True:
    Random_number_1=int(input("Enter your random number 1: "))
    operator=input("enter your opeartor +,-,X,/ and Q to quit : ")

    if operator=="Q":
        print("Thank you for taking part the calcultor will switch off now!")
        break
    Random_number_2=int(input("Enter you secound random number: "))

    if operator=="+":
        print(Random_number_1+Random_number_2)

    elif operator== "-":
        print(Random_number_1-Random_number_2)

    elif operator=="x":
        print(Random_number_1*Random_number_2)

    elif operator=="/":
        print(Random_number_1/Random_number_2)





