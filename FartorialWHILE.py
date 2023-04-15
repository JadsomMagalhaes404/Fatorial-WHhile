numero = int(input("Digite o valor do fatorial: "))
fat = 1
aux = 1
while numero <= 0:
    print("Valor 0 ou negativos não são permitidos")
    numero = int(input("Digite o valor do fatorial: "))
if numero > 0:
    while aux <= numero:
        fat *= aux
        aux += 1
        print(fat)
