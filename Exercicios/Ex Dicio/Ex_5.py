# Pede a palavra ao utilizador
palavra = "banana" 

# Cria o dicionário para a contagem
contagem_letras = {}

# Itera sobre cada letra da palavra
for letra in palavra:
    # Atualiza a contagem. Usa .get() para obter o valor atual (0 se a chave não existir)
    contagem_letras[letra] = contagem_letras.get(letra, 0) + 1

# Imprime o resultado
print(f"Entrada: \"{palavra}\"")
print(f"Resultado: {contagem_letras}")