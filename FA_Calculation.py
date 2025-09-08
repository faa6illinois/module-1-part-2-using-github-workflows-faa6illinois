import datetime 
from datetime import date

#Take user input in specified format
date_of_birth = input("Enter your date of birth in '(MM/DD/YYYY)' format:")


#Convert DOB to date
convert_date = datetime.strptime(date_of_birth, "%m/%d/%Y").date()


today = date.today()


calculate_days = today - convert_date

print(f"You are: {calculate_days} days old!")
