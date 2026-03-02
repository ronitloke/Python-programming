def fibo(n):
#     for i in range(1,10):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2) #n is the position of no
        #eg: for n0 9 fibo(9-1)+fibo(9-2)
        #                  21+13=34 on 9th position
# print(fibo(5))
# print(fibo(4))
# print(fibo(3))
# print(fibo(2))
# print(fibo(1))
for i in range(1,10):
    print(fibo(i))




