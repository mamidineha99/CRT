'''
1) write a python code to count the digits of number?
Ex: 15678 --> output:5
2)sum of the digits of a number?
Ex: 12345-->1=2=3=4=5=15
3) product of the digits of a number?
4)reverse the number?
5)count the number of even and odd digits '''
num = 15678
count = len(str(num))
print(f"Number of digits: {count}")
#2
num = 12345
digit_sum = sum(int(digit)for digit in str(num))
print(f"Sum of digits:{d_s}")
#3
num = 15678
sum = 1
while num>0:
    sum *=num%10
      
num = 15678
reversed_num = int(str(num)[::-1])
print(f"Reversed Number: {reversed_num}")

