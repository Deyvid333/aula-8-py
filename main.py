import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    print(produtos)
    return produtos

# produtos = carregar_produtos()
# print(produtos)

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()



def modificar_produtos():
    produtos = (carregar_produtos())
    pesquisa = input("Digite o nome do produto que voce quer modificar: ")

    pesquisa_nome = int(input("Digite 1 se voce quer mudar o nome do produto e 0 se voce nao quer mudar : "))
    for produto in produtos :
        if pesquisa.lower() == produto["nome"].lower() :
            if pesquisa_nome == 1 :
                novo_nome = input("Digite o novo nome do seu produto: ")
                produto["nome"] = novo_nome
                (salvar_produtos(produtos))
                break


    pesquisa_categoria = int(input("Digite 1 se voce quer mudar a categoria do produto e 0 se voce nao quer mudar : "))
    for produto in produtos :
        if pesquisa.lower() == produto["nome"].lower() :
            if pesquisa_categoria == 1 :
                nova_categoria = input("Digite a nova categoria do seu produto: ")
                produto["categoria"] = nova_categoria
                break


    pesquisa_preco = int(input("Digite 1 se voce quer mudar o preço do produto e 0 se voce nao quer mudar : "))
    for produto in produtos :
        if pesquisa.lower() == produto["nome"].lower() :
            if pesquisa_preco == 1 :
                novo_preco = int(input("Digite o novo preço do seu produto: "))
                produto["preco"] = novo_preco
                break


    pesquisa_nome = int(input(("Digite 1 se voce quer mudar o estoque do produto e 0 se voce nao quer mudar : ")))
    for produto in produtos :
        if pesquisa.lower() == produto["nome"].lower() :
            if pesquisa_estoque == 1 :
                novo_estoque = int(input("Digite o novo estoque do seu produto: "))
                produto["estoque"] = novo_estoque
                break

    
    

def excluir_produtos():
    produtos = (carregar_produtos())
    pesquisa = input("Digite o nome do produto que voce deseja excluir: ")
    for produto in produtos:
        print("comparando:", pesquisa.lower(), "com", produto["nome"].lower())
        if pesquisa.lower() == produto["nome"].lower():
            produtos.remove(produto)
            (salvar_produtos(produtos))
            break

def filtrar_produtos():
    produtos = (carregar_produtos())
    pesquisa = input("Digite o nome da categoria que voce deseja filtrar(Periféricos/Monitores/Armazenamento/Hardware/Redes) : ")
    for produto in produtos :
        if pesquisa.lower() == produto["categoria"].lower():
            print(produto)

def criar_produtos():
    produtos = (carregar_produtos())
    nome_produto = input("Digite o nome do seu produto: ")
    categoria_produto = input("Digite a categoria do seu produto (Periféricos/Monitores/Armazenamento/Hardware/Redes) : ")
    preco_produto = int(input("Digite o preço do seu produto: "))
    estoque_produto = int(input("Digite o estoque do seu produto: "))

    novo_produto = {
        "id": len(produtos) + 1,
        "nome": nome_produto,
        "categoria": categoria_produto,
        "preco": preco_produto,
        "estoque": estoque_produto
    }

    produtos.append(novo_produto)
    (salvar_produtos(produtos))


print("CONTROLE DE ESTOQUE EFICIENTE")
print("asinale a opção desejada abaixo: ")
print("Digite 0 Para sair do programa")
print("Digite 1 Para ver o estoque")
print("Digite 2 Para modificar um item do estoque")
print("Digite 3 Para excluir um item do estoque")
print("Digite 4 Para criar um item no estoque")
print("Digite 5 Para ver as opções novamente")
print("Digite 6 Para filtrar por categoria")




while True:
    escolha = int(input("Digite o numero da opção desejada: "))
    if escolha == 0:
        print("saindo do programa...")
        break

    elif escolha == 1 :
        carregar_produtos()

    elif escolha == 2 :
        modificar_produtos()

    elif escolha == 3 :
        excluir_produtos()

    elif escolha == 4 :
        criar_produtos()

    elif escolha == 5 :
        print("CONTROLE DE ESTOQUE EFICIENTE")
        print("asinale a opção desejada abaixo: ")
        print("Digite 0 Para sair do programa")
        print("Digite 1 Para ver o estoque")
        print("Digite 2 Para modificar um item do estoque")
        print("Digite 3 Para excluir um item do estoque")
        print("Digite 4 Para criar um item no estoque")
        print("Digite 5 Para ver as opções novamente")
        print("Digite 6 Para filtrar por categoria")


    elif escolha == 6 :
        filtrar_produtos()


