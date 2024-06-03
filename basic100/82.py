n = int(input())

for i in range(1,n+1):
    if(i<10):
        if(i%3==0 or i%6==0 or i%9==0):
            print('X', end=' ')
        else:
            print(i, end=' ')
    else:
        if(i%10==3 or i%10==6 or i%10==9):
            print('X', end=' ')

        else:
            print(i, end=' ')