fila = [("Tarefa 1", 5), ("Tarefa 2", 3)]
tempo = 3

while fila:
    tarefa, duracao = fila.pop(0)
    if duracao > tempo:
        print(f"Executando {tarefa} por {tempo} unidades de tempo.")
        fila.append((tarefa, duracao - tempo))
    else:
        print(f"Tarefa {tarefa} concluída.")
