n = int(input())

sum=0
i=1


while(True):

    sum+=i
    if(sum<n):
        i+=1
    else:
        break


print(i)