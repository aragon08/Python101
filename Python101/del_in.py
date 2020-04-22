# del & in

curso = 'python'
new_list = list(curso)
print(new_list)

del new_list[0]
print(new_list)

print('y' in curso)

print('a' in curso)

if 'y' in new_list:
    print('y es parte de la lista')

if 'a' in new_list:
    print('a no es parte de la lista')
