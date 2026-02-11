name=input('\nEnter your name:')
print("\nWelcome to the digital calculator programme,"+name+"!")
while True:
      print("\nA list of containing choices is shown below:")
      print("\nChoose one of the following options(1-7):\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Mod\n6.Power\n7.Exit")
      choice=int(input("\nEnter your choice:"))
      
      if choice>=1 and choice<=6:
         num1=int(input("\nEnter first number:"))
         num2=int(input("\nEnter second number:"))


         if   choice==1:
              print("\nThe result is:",num1+num2)
         elif choice==2:
              print("\nThe result is:",num1-num2)
         elif choice==3:
              print("\nThe result is:",num1*num2)
         elif choice==4:
              
              if num2==0:
                  print("\nThe division cannot be executed and will result in undefined result")
              else:
                  div=num1/num2
                  print("\nThe result is:"+f"{div:.2f}")


         elif choice==5:
              print("\nThe result is:",num1%num2)
         elif choice==6:
              power=pow(num1,num2)
              print("\nThe result is:"+f"{power:.2f}")
          

      elif choice ==7:
           print("\nThanks for using the calculator")
           break
         


      else:
           print("\nInvalid choice input\tTry again!") 



print("\nThank you")
