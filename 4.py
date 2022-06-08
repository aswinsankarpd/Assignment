def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

num = int(input("Enter number: "))
mul = 1

for i in range(1,num+1):
    mul = mul*factorial(i)
print(mul)