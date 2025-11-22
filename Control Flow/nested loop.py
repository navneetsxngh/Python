# for i in range(1,4):
#     for j in range(1,4):
#         print(i,',',j, end='  ')
#     print(' ')

## Prime numbers from 1 to N
# num = int(input("Enter Limit: "))

# for i in range(2,num+1):
#     count = 0
#     for j in range(2,i):
#         if i % j == 0:
#             count += 1
#     if count == 0:
#         print(i)

n = int(input("Enter limit: "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i >= j:
            print('*', end=' ')
    print('')