w, h, b = input().split(' ')
w=int(w)
h=int(h)
b=int(b)

storage=round(w*h*b/8/1024/1024, 2)
print(f"{storage:.2f} MB")