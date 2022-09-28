
x=1
while x==1:
    c=int(input('Enter 1 to continue , 0 to stop: '))
    if c==1 :
        print("Select an operation to perform :  ")
        print("1.ADD")
        print("2.SUBTRACT")
        print("3.MULTIPLY")
        print("4.DIVIDE")
        operation = int(input("Enter the number that indicates the operation that you want : "))
        num1 = int(input("enter number 1 : "))
        num2 = int(input("enter number 2 : "))
        if operation==1 :
           print("The result of add numbers : ",num1+num2)
        elif operation==2 :
           print("The result of subtracting numbers : ",num1-num2)
        elif operation==3 :
           print("The result of multiplying numbers : ",num1*num2)
        elif operation==4 :
           print("The result of divide numbers : ",num1/num2)
        else :
          print("Invalid Entry")
    elif c==0:
        print('See you soon')
        break



