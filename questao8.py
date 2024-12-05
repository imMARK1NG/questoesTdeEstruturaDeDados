def verificar_parenteses(expressao):
    pilha = []
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return False
            pilha.pop()
    return not pilha

print(verificar_parenteses("a + b * (c)")) 
