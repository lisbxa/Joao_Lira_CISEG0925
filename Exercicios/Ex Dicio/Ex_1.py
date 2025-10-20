# Criar o dicionário principal para armazenar os alunos
alunos = {}

# Inserir alunos
# Vamos inserir 3 alunos como exemplo
alunos[1] = {'nome': 'Maria', 'idade': 20, 'curso': 'Engenharia'}
alunos[2] = {'nome': 'Pedro', 'idade': 22, 'curso': 'Informática'}
alunos[3] = {'nome': 'Ana', 'idade': 19, 'curso': 'Gestão'}

# Listar e imprimir cada elemento no formato desejado
print("--- Lista de Alunos ---")
for id_aluno, dados in alunos.items():
    print(f"Aluno {id_aluno}:")
    print(f"nome: {dados['nome']}")
    print(f"idade: {dados['idade']}")
    print(f"curso: {dados['curso']}")
    print("-" * 10)