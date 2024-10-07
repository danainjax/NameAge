from datetime import date

name = input('What is your name? ')
age = int(input('How old are you? '))
current_year = date.today().year
year_born = current_year - age
print(f"Hello {name}! You were born in {year_born}.")