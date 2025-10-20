d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

# Cria um novo dicionário juntando d1 e d2
# Opção 1 (a mais moderna): Usando o operador de desempacotamento **
d_junto = {**d1, **d2}

# Opção 2 (alternativa): Usando .copy() e .update()
# d_junto = d1.copy()
# d_junto.update(d2)

# Imprime o resultado
print(d_junto)