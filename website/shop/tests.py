string = 'Барабанщик бил бой в барабан'
if string.count('ра') is False:
    print(-1)
else:
    for i, d in enumerate(string):
        if 'р' in d:
            print(i)
