d = {'a': 1, 'b': 2, 'c': 3}

# Cria um novo dicionário invertido
# Usa uma compreensão de dicionário: {valor: chave for chave, valor in d.items()}
d_invertido = {valor: chave for chave, valor in d.items()}

# Imprime o resultado
print(f"Dicionário original: {d}")
print(f"Dicionário invertido: {d_invertido}")