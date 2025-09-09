from datetime import datetime, date

#Take user input in specified format
date_of_birth = input("Enter your date of birth in '(MM/DD/YYYY)' format:")


#Convert DOB to date
convert_date = datetime.strptime(date_of_birth, "%m/%d/%Y").date()


today = date.today()


calculate_days = (today - convert_date).days

#Print both input and output
print(f"Your birthday is on {date_of_birth} and you are {calculate_days} days old!")
