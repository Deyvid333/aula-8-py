import json

def carregar_produtos():
    arquivo = open("produto.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

produtos = carregar_produtos()
print(produtos)

def salvar_produtos(produtos):
    arquivo = open("produto.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

def excluir_produtos():
    arquivo = open("produto.json", "w", encoding="utf-8")
    pesquisa = input("Digite o nome do produto que voce deseja excluir: ")
    produtos = json.load(arquivo)
    for produto in produtos:
        if pesquisa.lower() == produto["nome"].lower()
            produtos.remove(produto)
            print(produtos)



print("CONTROLE DE ESTOQUE EFICIENTE")
print("asinale a opção desejada abaixo: ")
print("Digite 0 Para sair do programa")
print("Digite 1 Para ver o estoque")
print("Digite 2 Para modificar um item do estoque")
print("Digite 3 Para excluir um item do estoque")
print("Digite 4 Para criar um item no estoque")
print("Digite 5 Para ver as opções novamente")

escolha = input("Digite o numero da opção desejada: ")

while True:
    if escolha == 0:
        print("saindo do programa...")
        break

    elif escolha == 1 :
        carregar_produtos()

    elif escolha == 2 :
        salvar_produtos()


