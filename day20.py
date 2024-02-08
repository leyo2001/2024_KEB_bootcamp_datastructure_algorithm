from random import randint

a= randint(1,100)
counter = 7

while(counter != 0):

    print(f"남은기회: {counter}")
    counter -= 1

    b=int(input("예상숫자: "))

    if(b>a):
        print("down")

    elif(b<a):
        print("up")

    else:
        print("정답")
        break

else:
    print("fail!")