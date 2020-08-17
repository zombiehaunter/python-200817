grade=int(input("ur grade: "))

if grade >=0 and grade <=100:
    if grade >=90:
        print("level a")
    elif grade >=80:
        print("level b")
    elif grade >=70:
        print("level c")
    elif grade >=60:
        print("level d")
    else:
        print("level e")
       
else:
    print("error")