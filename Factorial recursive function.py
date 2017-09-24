# An example of a recursive function to
# find the factorial of a number

def calc_factorial(x):

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))

num = float(input('Enter a number: '))

if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

print("The factorial of", num, "is", calc_factorial(num))		
print("This is always printed.")
