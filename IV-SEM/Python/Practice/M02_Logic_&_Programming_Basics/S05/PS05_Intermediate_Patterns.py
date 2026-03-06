'''li = ['1','2','3','4','5','6']
    output = ['1','4','9','16','25','36']
    '''
'''
3.diamond
n=4
output:
  
   * 
  * *
 * * *
* * * *
 * * *
  * *
   *
   '''
'''
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)
'''
'''
output:
   1
  1 2
 1 2 3
1 2 3 4
'''
n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
#n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+" ".join([str(k) for k in range(1,i+1)]))