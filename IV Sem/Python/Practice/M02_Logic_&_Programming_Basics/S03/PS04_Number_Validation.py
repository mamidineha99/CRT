#perfect number
'''n = int(input())
s = 0
for i in range(1,n//2+1):
    if n%i==0:
        s+=i
print("perfect" if n==s else "not perfect")'''
#strong number
def factorial(n):
    if n < 0:
        return "no factorial for -ve"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact
    