pilha_undo = []
pilha_redo = []


acao = "ação"  
pilha_undo.append(acao)
pilha_redo.clear()

if pilha_undo:
    pilha_redo.append(pilha_undo.pop())

if pilha_redo:
    pilha_undo.append(pilha_redo.pop())

print(f"Pilha de desfazer: {pilha_undo}")
print(f"Pilha de refazer: {pilha_redo}")
