# SYNTAX :
# def function_name(param1, param2):
#     # Some work
#     return Value
# function_name(arg1,arg2) # function call

# Create the function
# def calc_sum(a,b):
#     sum = a + b
#     return sum
# print(calc_sum(5,10))


# default argument

# def cal_prod(a=4,b=2):
#     print(a*b)
# cal_prod()


# WAP to print the length of a list
# cities = ["Delhi", "Kaimganj", "Krishna Nagar", "Farrukhabad","Noida"]
# heroes = ["Thor","Ironman","Spiderman","Hons"]
# def print_len(list):
#     print(len(list))
# print_len(cities)
# print_len(heroes)


# # WAP to print the elements of a list in a single line
# cities = ["Delhi", "Kaimganj", "Krishna Nagar", "Farrukhabad","Noida"]

# def print_list(list):
#     for item in list:
#         print(item, end=" ")
# print_list(cities)


#
user_usd = int(input("Enter amount in USD: "))


def converter(usd_val):
    inr_val = usd_val * 90
    print(usd_val, "USD", inr_val, "INR")

converter(user_usd)
