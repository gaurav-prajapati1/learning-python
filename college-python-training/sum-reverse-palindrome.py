# # Sum of digits

# n = int(input("Enter a number: "))

# sum = 0

# while n > 0:
#     digit = n % 10
#     sum = sum + digit
#     n = n // 10

# print("Sum of digits =", sum)




# Reverse a number

# n = int(input("Enter a number: "))

# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10

# print("Reverse =", reverse)




# Check whether a number is a Palindrome
 
n = int(input("Enter a number: "))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print("Palindrome number")
else:
    print("Not a Palindrome number")