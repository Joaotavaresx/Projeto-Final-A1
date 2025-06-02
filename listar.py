from estoque import estoque  # Importa a lista 'estoque' do módulo estoque.py

def listar_produtos():
    """
    Lista todos os produtos disponíveis no estoque.
    Exibe as informações de cada produto formatadas de forma organizada.
    """
    
    # Verifica se o estoque está vazio
    if not estoque:
        print("⚠️ Estoque vazio.")  # Mensagem de aviso caso não haja produtos
    else:
        print("📦 Produtos no Estoque:")  # Título da listagem
        print("-" * 40)  # Linha separadora visual
        
        # Percorre a lista de produtos no estoque
        for produto in estoque:
            # Exibe o código do produto
            print(f"Código: {produto['codigo']}")
            
            # Exibe o nome do produto
            print(f"Nome: {produto['nome']}")
            
            # Exibe a quantidade disponível em estoque
            print(f"Quantidade: {produto['quantidade']}")
            
            # Exibe o preço formatado com duas casas decimais
            print(f"Preço: R$ {produto['preco']:.2f}")
            
            # Linha separadora entre produtos
            print("-" * 40)
