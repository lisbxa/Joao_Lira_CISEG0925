import json
import re

# ========== Exercício 1: Ler o ficheiro JSON ==========
with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

# ========== Regex ==========
regex_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
regex_nif = r'^[123568]\d{8}$'
regex_telemovel = r'\d'  # vamos contar apenas os dígitos

# ========== Exercício 2: Validar emails ==========
def validar_email(email):
    return re.match(regex_email, email) is not None

# ========== Exercício 3: Extrair domínios ==========
def extrair_dominio(site):
    return site.replace("http://", "").replace("https://", "").split("/")[0]

# ========== Exercício 4: Validar NIF ==========
def validar_nif(nif):
    return re.match(regex_nif, nif) is not None

# ========== Validar Telemóvel ==========
def validar_telemovel(telemovel):
    apenas_digitos = re.sub(r'\D', '', telemovel)  # remove tudo que não é dígito
    return len(apenas_digitos) == 9

# ========== Exercício 5: Guardar registos válidos ==========
dados_validos = []
for pessoa in dados:
    email_ok = validar_email(pessoa["email"])
    nif_ok = validar_nif(pessoa["nif"])
    tel_ok = validar_telemovel(pessoa["telemovel"])
    
    print(f"🔎 {pessoa['nome']}: email={email_ok}, nif={nif_ok}, telemovel={tel_ok}, dominio={extrair_dominio(pessoa['site'])}")

    if email_ok and nif_ok and tel_ok:
        dados_validos.append(pessoa)

# Guardar no ficheiro JSON
with open("dados_validos.json", "w", encoding="utf-8") as f:
    json.dump(dados_validos, f, indent=2, ensure_ascii=False)

# ========== Exercício 6: Criar ficheiro TXT ==========
with open("dados.txt", "w", encoding="utf-8") as f:
    for pessoa in dados_validos:
        f.write(f"{pessoa['nome']} - {pessoa['email']}\n")

print("\n✅ Processamento concluído!")
print("→ Ficheiro 'dados_validos.json' criado com registos válidos.")
print("→ Ficheiro 'dados.txt' criado com nome e email.")
