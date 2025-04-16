print("Welcome to ATM")
Balance =5000
while True:
    i=int(input("How can i help you......\n 1 for Check Bank Balance \n 2 for Withdraw money \n 3 for Deposit money \n 4 for EXIT\n"));
    if i == 1:
        {
            print("Balance:",Balance)
        }
    elif i == 2:
         withdraw = int(input("How much ammount you want to withdraw:"))
         if Balance>=withdraw:
             Balance=Balance-withdraw
             print("Your updated Balance after withdraw : ",Balance)
         else:
             print("you don't have enough Balance\n Your Balance in Account :",Balance)
    elif i == 3:
        Deposit = int(input("How much ammount you want to deposit: "))
        Balance = Balance+Deposit
        print("You Balance after Deposit : ",Balance)
    elif i == 4:
        print("Thank you for using ATM")
        break
    else:
        print("Invalid choice,\n Please choose right choice.")

        
        
    