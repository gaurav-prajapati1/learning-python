name = input("What is your name? ")
birth_year = input("What year were you born? ")
age = 2026 - int(birth_year)
if age >= 18:
    status = "You are adult"
else:
    status = "You are minor "
print(f"Hello {name}! You are {age} years old, which means you are {status}.")