name=input("\nEnter your name:")
age=int(input("\nEnter your age:"))
height=float(input("\nEnter your height(meter)"))
is_student=input("\nAre you a student?(yes/no)")
print("\nYour name is:"+name)
print("\nYour age is:"+str(age))
print("\nYour height is(meter):"+str(height))
if is_student.lower()=="yes":
   print("\nYou are a student")
   is_student=True 
else:
   print("\nYou are not a student")
   is_student=False
#Bonus
height1=(height*100)
print("\nYour converted height is"+str(height1))
if is_student==True:
   print("\nStudent life is one of the major periods of human life")

