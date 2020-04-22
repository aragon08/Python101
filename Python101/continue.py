n = int(input('escriba numero: '))
for item in range(1,n+1):
    if item%2==0:
        continue #Salta a la siguiente instruccion
        print(item)
    else:
        print(item)