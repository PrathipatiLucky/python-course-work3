
data = {
    'lucky':{'status':True,'python':90,'mysql':95,'flask':98,},
    'eswar':{'status':False,'python':None,'mysql':None,'flask':None,},
    'vardhan':{'status':True,'python':20,'mysql':35,'flask':38,},
    'mithra':{'status':True,'python':60,'mysql':65,'flask':68,},
    'nandan':{'status':True,'python':70,'mysql':75,'flask':78,},
    'deva':{'status':True,'python':80,'mysql':85,'flask':88,}
}

name = input("Enter the name: ")
if name in data:
    if data [name]['status']:
        sum = data[name]['python'] + data[name]['mysql'] + data[name]['flask']
        avg = sum/3
        print(f"Hello {name}!!!")
        print(f"Your average score is {avg}")
        if avg >=90:
            print("Outstanding performance")
        elif avg >= 80:
            print("Very Good")
        elif avg >=70:
            print("Good, work hard")
        elif avg >=35:
            print("Better luck next time")
        else:
            print("You failed yhe Exam")

    else:
        print(f'{name} did not attend the exam, bring your parents')
else:
    print(f"Name {name } not found in the data")