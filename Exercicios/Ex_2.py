mensagem = "Olá Mundo"
chave = "chave"
codigos = []
mensagem_final = ""

def criptografar(mensagem, chave):
    if not chave:
        raise ValueError("A chave não pode ser vazia!")

    chave_num = sum(ord(c) for c in chave)
    criptografada = []
    for c in mensagem:
        codigo = ord(c) + chave_num
        # rotação no intervalo ASCII visível (32–126)
        codigo_rot = 32 + ((codigo - 32) % 95)
        criptografada.append(codigo_rot)
    return criptografada


def descriptografar(codigos, chave):
    if not chave:
        raise ValueError("A chave não pode ser vazia!")

    chave_num = sum(ord(c) for c in chave)
    mensagem = ""
    for codigo in codigos:
        original = codigo - chave_num
        # rotação no intervalo ASCII visível (32–126)
        original_rot = 32 + ((original - 32) % 95)
        mensagem += chr(original_rot)
    return mensagem



print("Mensagem original:", mensagem)
codigos = criptografar(mensagem, chave)
print("Criptografada (lista de códigos):", codigos)
mensagem_final = descriptografar(codigos, chave)
print("Descriptografada:", mensagem_final)