notas = {
    'João': [7, 8, 9],
    'Maria': [10, 9, 8],
    'Ana': [6, 7, 8]
}

print("--- Médias dos Alunos ---")
# Itera sobre o dicionário de notas
for aluno, lista_notas in notas.items():
    # Calcula a soma das notas
    soma_notas = sum(lista_notas)
    # Calcula o número de notas
    num_notas = len(lista_notas)
    # Calcula a média (verifica se há notas para evitar divisão por zero)
    media = soma_notas / num_notas if num_notas > 0 else 0

    # Imprime no formato desejado, formatando a média para uma casa decimal
    print(f"{aluno}: {media:.1f}")