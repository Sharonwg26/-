v = int(input('Input： '))
c=0
for i in range(v):
    if i % 3 == 0 and i % 5 ==0:
        c+=1
    elif i % 3 != 0 and i % 5 != 0:
        c+=1
print(c)
