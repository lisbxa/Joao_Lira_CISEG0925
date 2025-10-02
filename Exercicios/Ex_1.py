nom_comp = ""
nome_valido = True

nom_comp = input("Por favor, insira o seu nome completo: ")

for i in range(len(nom_comp)):
    caractere = nom_comp[i]
    codigo_ascii = ord(caractere)

    if i == 0:
        if 65 <= codigo_ascii <= 90:
            continue
        else:
            print("Nome inválido: a primeira letra deve ser maiúscula.")
            nome_valido = False
            break

    if i > 0 and nom_comp[i-1] == ' ':
        if 65 <= codigo_ascii <= 90:
            continue
        else:
            print("Nome inválido: a letra após o espaço deve ser maiúscula.")
            nome_valido = False
            break

    if 97 <= codigo_ascii <= 122 or codigo_ascii == 32:
        continue
    else:
        print("Nome inválido: contém caracteres não permitidos.")
        nome_valido = False
        break

if nome_valido and len(nom_comp) > 0:
    print("Nome válido!")