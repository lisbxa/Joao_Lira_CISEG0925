from collections import defaultdict

# ----------------------------------------------------------------------
# 1. Ordenar por ordem alfabética (A -> Z) - Implementação Manual (Exemplo)
# ----------------------------------------------------------------------

def ordenar_a_z_manual(lista_palavras):
    """
    Ordena uma lista de palavras A->Z usando um Bubble Sort simples
    para simular a comparação caractere por caractere (como solicitado).
    """
    n = len(lista_palavras)
    # Loop de Bubble Sort
    for i in range(n):
        for j in range(0, n - i - 1):
            palavra_a = lista_palavras[j]
            palavra_b = lista_palavras[j + 1]

            # Simulação da comparação caractere por caractere e regra do prefixo
            if palavra_a > palavra_b:  # Python já faz a comparação lexicográfica
                # Troca se a palavra_a for "maior" (vier depois alfabeticamente)
                lista_palavras[j], lista_palavras[j + 1] = lista_palavras[j + 1], lista_palavras[j]

    return lista_palavras

# ----------------------------------------------------------------------
# 2. Ordenar por ordem alfabética inversa (Z -> A), ignorando maiúsculas/minúsculas
# ----------------------------------------------------------------------

def ordenar_z_a_case_insensitive(lista_palavras):
    """
    Ordena uma lista Z->A, ignorando o case, usando uma chave de ordenação.
    """
    # key=str.lower: Normaliza para minúsculas APENAS para a comparação.
    # reverse=True: Ordena da maior (Z) para a menor (A).
    resultado = sorted(lista_palavras, key=str.lower, reverse=True)
    return resultado

# ----------------------------------------------------------------------
# 3. Ordenar os caracteres de uma palavra por ordem alfabética
# ----------------------------------------------------------------------

def ordenar_caracteres(palavra):
    """
    Pega numa palavra, divide em caracteres, ordena-os e junta-os novamente.
    """
    # 1. Divide a palavra em caracteres
    caracteres = list(palavra)
    
    # 2. Ordena os caracteres (ordenação por ASCII/Unicode)
    caracteres_ordenados = sorted(caracteres)
    
    # 3. Junta novamente numa string
    resultado = "".join(caracteres_ordenados)
    return resultado

# ----------------------------------------------------------------------
# 4. Ordenar uma lista de palavras pela quantidade de letras minúsculas
# ----------------------------------------------------------------------

def contar_minusculas(palavra):
    """Função auxiliar que conta o número de letras minúsculas em uma palavra."""
    count = 0
    for char in palavra:
        # Verifica se o código ASCII (ord) está no intervalo de 'a' a 'z'
        # ou usa o método islower() para ser mais robusto.
        if char.islower(): 
            count += 1
    return count

def ordenar_por_qtd_minusculas(lista_palavras):
    """
    Ordena a lista usando a contagem de minúsculas como chave (do menor para o maior).
    """
    # key=contar_minusculas: Usa o resultado da função de contagem como peso/chave.
    resultado = sorted(lista_palavras, key=contar_minusculas)
    return resultado

# ----------------------------------------------------------------------
# 5. Agrupar palavras pela letra inicial e ordenar cada grupo (A -> Z)
# ----------------------------------------------------------------------

def agrupar_e_ordenar(lista_palavras):
    """
    Agrupa as palavras pela primeira letra e ordena as listas internas.
    """
    # Cria um dicionário que inicializa o valor como uma lista vazia (defaultdict)
    grupos = defaultdict(list)
    
    # 1. Agrupamento
    for palavra in lista_palavras:
        # Pega a primeira letra em minúsculas para o agrupamento
        primeira_letra = palavra[0].lower()
        grupos[primeira_letra].append(palavra)
        
    # 2. Ordenação Interna e Conversão para dicionário normal
    resultado_final = {}
    
    # Ordena as chaves do dicionário (opcional, para um output mais limpo)
    for chave in sorted(grupos.keys()):
        # Ordena a lista de palavras para cada grupo A->Z
        lista_ordenada = sorted(grupos[chave])
        resultado_final[chave] = lista_ordenada
        
    return resultado_final

# ----------------------------------------------------------------------
# Testes com os exemplos fornecidos
# ----------------------------------------------------------------------

print("--- 1. Ordenar A -> Z (Implementação Manual) ---")
lista_1 = ["banana", "uva", "abacaxi", "laranja"]
# Nota: É preciso passar uma cópia se quisermos usar o original mais tarde
print(f"Original: {lista_1}")
print(f"Resultado: {ordenar_a_z_manual(lista_1.copy())}\n") # .copy() para não alterar a original

print("--- 2. Ordenar Z -> A, Ignorando Case ---")
lista_2 = ["Python", "inteligência", "Aprender", "dados", "Rede"]
print(f"Original: {lista_2}")
print(f"Resultado: {ordenar_z_a_case_insensitive(lista_2)}\n")

print("--- 3. Ordenar Caracteres de uma Palavra ---")
palavra_3 = "algoritmo"
print(f"Original: {palavra_3}")
print(f"Resultado: {ordenar_caracteres(palavra_3)}\n")

print("--- 4. Ordenar pela Quantidade de Minúsculas ---")
lista_4 = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]
print(f"Original: {lista_4}")
print(f"Resultado: {ordenar_por_qtd_minusculas(lista_4)}\n")

print("--- 5. Agrupar pela Inicial e Ordenar Grupos ---")
lista_5 = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
print(f"Original: {lista_5}")
resultado_5 = agrupar_e_ordenar(lista_5)
print("Resultado:")
for chave, valor in resultado_5.items():
    print(f"  '{chave}': {valor}")