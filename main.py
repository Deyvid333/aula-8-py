import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

# produtos = carregar_produtos()
# print(produtos)

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

# def excluir_produtos():
#     arquivo = open("produtos.json", "r", encoding="utf-8")
#     produtos = json.load(arquivo)
#     arquivo.close()
#     pesquisa = input("Digite o nome do produto que voce deseja excluir: ")
#     for produto in produtos:
#         if pesquisa.lower() == produto["nome"].lower():
#             produtos.remove(produto)
#             arquivo = open("produto.json", "w", encoding="utf-8")
#             json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
#             arquivo.close()
#             print("Produto Removido com sucesso!")
#             break

def excluir_produtos():
    produtos = (carregar_produtos())
    pesquisa = input("Digite o nome do produto que voce deseja excluir: ")
    for produto in produtos:
        if pesquisa.lower() == produto["nome"].lower():
            produtos.remove(produto)
            (salvar_produtos())
            break


print("CONTROLE DE ESTOQUE EFICIENTE")
print("asinale a opção desejada abaixo: ")
print("Digite 0 Para sair do programa")
print("Digite 1 Para ver o estoque")
print("Digite 2 Para modificar um item do estoque")
print("Digite 3 Para excluir um item do estoque")
print("Digite 4 Para criar um item no estoque")
print("Digite 5 Para ver as opções novamente")



while True:
    escolha = int(input("Digite o numero da opção desejada: "))
    if escolha == 0:
        print("saindo do programa...")
        break

    elif escolha == 1 :
        carregar_produtos()

    elif escolha == 2 :
        salvar_produtos()

    elif escolha == 3 :
        excluir_produtos()


