from collections import deque

fila_clientes = deque()

def adicionar_cliente(nome):
    fila_clientes.append(nome)

def atender_cliente():
    if fila_clientes:
        return f"Cliente {fila_clientes.popleft()} atendido."
    return "Nenhum cliente na fila."

adicionar_cliente("Pedro")
adicionar_cliente("Ana")
adicionar_cliente("Andressa")

print(atender_cliente()) 

print(f"\nPessoas na fila \n\t{fila_clientes}")