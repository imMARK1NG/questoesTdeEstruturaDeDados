def executar_processos(fila, tempo):
    while fila:
        processo, duracao = fila.pop(0)
        if duracao > tempo:
            print(f"Executando {processo} por {tempo} unidades de tempo.")
            fila.append((processo, tempo - duracao))
        else:
            print(f"{processo} concluído.")

fila = [("Processo 1", 6), ("Processo 2", 3)]
executar_processos(fila, 3)
