n = int(input('ingresa numero: '))
for item in range(1,n+1):
    if not(item % 2) & (item %6):
        continue
    if item % 6==0:
        break
    print(item)
 
