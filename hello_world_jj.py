# Ask user for their Name
name = input("What is your name? ")
# Ask user for their Birth_year = ....
birth_year = input("what is your Birth Year? ")
#say hello to the user
print(f'hello,{name}!')
#pull todays date
from datetime import datetime
this_year = datetime.now().year
#return a reply for how old you think the user is by calc his year - current year
age = this_year - int(birth_year)
print(f"you must be {age}")
print("good bye")

