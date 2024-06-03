h, b, c, s = input().split(' ')
h=int(h)
b=int(b)
c=int(c)
s=int(s)

storage=h*b*c*s/8/1024/1024
print(f"{round(storage,1)} MB")