print("Welcome to the age calculator program!\n")
import datetime
b_year = int(input("Enter your birthyear: "))
b_month = int(input("\nEnter your birthmonth: "))
b_day= int(input("\nEnter your birthday: "))
birth_date = datetime.date(b_year,b_month,b_day)
today_date=datetime.date.today()
days_difference=(today_date - birth_date).days
age=days_difference //365 
print("Your age is "+ str(age))

