edad = int(input("your age..."))


if edad < 0 :
    print ("invalid_age")
elif edad < 12 :
    print ("discounted")
elif edad < 59 :
    print ("regualar price")
elif edad > 60 :
    print ("senior")
else :
    print("wrong answer")                                  

    print ("<-------------------------------------------------->") 
    #while#
while   True:
    num1 = float(input("1st digit"))
    num2 = float(input("2nd digit"))
    
    operation = input ("choose your operation +,-,%,*")

    if operation == "+":
        result = num1+num2
        print ("the answer is:", result)

    if operation =="-":
        result = num1+num2
        print("the answer is:", result)

    if operation == "%":
        result = num1%num2
        print ("the answer is:", result)

    if operation == "*":
        result =num1*num2
        print ("the answer is:", result)

    print ("<-------------------------------------------------------->") 
    #for#

    userquestion = input("Maglagay ng command o i-type ang 'quit':")

    if userquestion == "quit":
        print ("closing")
        break
    
    for letter in userquestion:
        print ("hiiii:  ", letter)

    print ("<------------------------------------------------------------>")
    #combination of for, while and condition
    mga_prutas = ["orange","banana","apple"]
    mga_gulay = ["talong","okra","kamatis"]


    while True:

        product = input("typehere:")

        if product in mga_prutas:
                print ("Masustansiya at matamis!")
        elif product in mga_gulay:
                print ("Puno ng bitamina!")
        else:
                print ("not_available")

