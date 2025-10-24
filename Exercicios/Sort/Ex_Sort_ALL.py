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

def ordenar_por_qtd_minusculas(