nomes = [
    "Pedro Pereira",
    "Ana Beatriz",
    "Ana Clara",
    "Carlos Silva",
    "Beatriz Souza",
    "Ana Paula",
    "Pedro Andrade",
]

nom = len(nomes) #

for i in range(nom):
    idx = i

    for a in range(i + 1, nom):
        if nomes[a] < nomes[idx]:
            idx = a

    nomes[i], nomes[idx] = nomes[idx], nomes[i]

for nome in nomes:
    print(nome)
