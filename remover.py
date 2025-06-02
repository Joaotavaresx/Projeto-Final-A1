from estoque import estoque

def remover_produto():
    """
    Remove um produto do estoque com base no código informado.
    """
    codigo = input("Digite o código do produto a ser removido: ")
     # Percorre a lista de produtos no estoque
    for produto in estoque:
     # Verifica se o código do produto atual corresponde ao código digitado
        if produto['codigo'] == codigo:
     # Remove o produto da lista 'estoque'
            estoque.remove(produto)
     # Informa ao usuário que o produto foi removido com sucesso       
            print("✅ Produto removido com sucesso.")
            return # Encerra a função após a remoção
     # Se o loop terminar sem encontrar o produto, exibe mensagem de erro       
    print("❌ Produto não encontrado.")
