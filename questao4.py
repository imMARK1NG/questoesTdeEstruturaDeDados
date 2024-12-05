from collections import deque

fila = deque()
fila.append(10)
fila.append(9)
fila.append(8)
fila.append(7)
fila.append(6)
fila.append(5)
fila.append(4)
fila.append(3)
fila.append(2)
fila.append(1)


maior = max(fila)
menor = min(fila)
media = sum(fila) / len(fila)


print(f"dados da fila: \n{fila}")
print(f"o maior valor na fila é {maior}")
print(f"o mennor valor na fila é {menor}")
print(f"a media é {media}")
print(f"a soma da fila é {sum(fila)}")