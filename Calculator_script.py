num1=int(input("Enter number1:\n"))
num2=int(input("Enter number2:\n"))
Calc=int(input("Choose any Option of Calculator as \n 1=Add\n 2=Subtract\n 3=Multiply\n 4=Divide\n"))
if Calc == 1:
    {
        print("Result:",num1+num2)
    }
elif Calc ==2:
    {
        print("Result:",num1-num2)
    }
elif Calc ==3:
    {
        print("Result:",num1*num2)
    }
elif Calc ==4:
    {
        print("Result:",num1/num2)
    }
else:
    {
        print("You entered Wrong Input \n Please enter right input")
    }
