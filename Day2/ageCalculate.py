from datetime import date

Dob =int(input("enter your Birth year "))
current_year=(date.today().year)

yourAge=current_year-Dob
print("your age is ", yourAge)