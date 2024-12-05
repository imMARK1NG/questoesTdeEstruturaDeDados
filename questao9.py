numero = int(input("Digite um valor:"))
pilha = []

while numero > 0:
    pilha.append(numero % 2)
    numero //= 2


binario = ''.join(map(str, pilha[::-1]))
print(f"binario: {binario}")
