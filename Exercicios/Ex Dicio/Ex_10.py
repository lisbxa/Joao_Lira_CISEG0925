# Pede a frase ao utilizador
# frase = input("Introduz uma frase: ").lower()
frase = "hoje é um bom dia e hoje o sol está a brilhar"

# 1. Limpar e dividir a frase em palavras
# Converte para minúsculas e remove pontuação básica antes de dividir (opcional mas recomendado)
# Simplificando, apenas dividimos por espaços e convertemos para minúsculas
palavras = frase.lower().split()

# 2. Cria o dicionário de contagem
contagem_palavras = {}

# Itera sobre cada palavra
for palavra in palavras:
    # Atualiza a contagem. Usa .get() para obter o valor atual (0 se a chave não existir)
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

# Imprime o resultado
print(f"Entrada: \"{frase}\"")
print(f"Resultado: {contagem_palavras}")