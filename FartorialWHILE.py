numero = int(input("Digite o valor do fatorial: "))
fat = 1
aux = 1
while aux <= numero:
    fat *= aux
    aux += 1
print(fat)