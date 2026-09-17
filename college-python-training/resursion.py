# Call by iself
def shown(n):
    if n == 0:
        return

    print(n)
    shown(n - 1)


shown(5)


n = int(input("Enter Your number:"))
def fact(n):
    if(n==1 or n==0):
         return n
    return fact(n-1) * n
print(fact(n))


# WAP to calculation sum of n natural number using recursion

def calc_sum(n):
     if (n==0):
          return 0
     return calc_sum(n-1) + n
sum = calc_sum(10)
print(sum)


# WAP print all the element in list using recursion

def print_list(list,index=0):
    if (index==len(list)):
        return
    print(list[index])
    print_list(list,index+1)

citeis = ["Delhi", "Farrukhabad", "Chennai", "Dehradun", "Goa", "Mumbai"]

print_list(citeis)
