numeros = []
for i in range(3):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)

multiplicados = [x * 2 for x in numeros]

print("Lista original:", numeros)
print("Lista multiplicada por 2:", multiplicados)
print("Soma dos números originais:", sum(numeros))
print("Soma dos números multiplicados por 2:", sum(multiplicados))