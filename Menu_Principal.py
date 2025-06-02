from estoque import adicionar_produto
from remover import remover_produto
from listar import listar_produtos

def menu():
    """
    Exibe o menu principal do sistema e direciona para a função escolhida.
    """
    while True:
        print("\n📋 Menu do Sistema de Estoque")
        print("1 - Adicionar Produto")
        print("2 - Remover Produto")
        print("3 - Listar Produtos")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            remover_produto()
        elif opcao == '3':
            listar_produtos()
        elif opcao == '4':
            print(" Saindo do sistema...")
            break
        else:
            print(" Opção inválida. Tente novamente.")
