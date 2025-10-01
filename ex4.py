nome = "SeuNomeAqui"  # substitua pelo seu nome real
contador = 0
for letra in nome:
    if letra.isalpha():
        contador += 1
print(f"O nome '{nome}' tem {contador} letras.")