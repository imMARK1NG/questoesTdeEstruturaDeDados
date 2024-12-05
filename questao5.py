from collections import deque


fila1 = deque()
fila2 = deque()

fila1.append(1)
fila1.append(2)
fila1.append(3)

fila2.append(4)
fila2.append(5)
fila2.append(6)

print(f"Dados da fila1:\n\t{fila1}")
print(f"\nDados da fila2:\n\t{fila2}")

fila3 = deque()

while fila2:
    fila1.append(fila2.popleft())
   
print(f"\nDados da fila1:\n\t{fila1}")
print(f"\nDados da fila2:\n\t{fila2}")

