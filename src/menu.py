def show_main_menu():
    """
    Função para mostrar o menu principal
    """
    size: int = 40 # largura maxima
    print("+" + "-"*size + "+")
    print("|" + " Menu principal ".center(size) + "|")
    print("+" + "-"*size + "+")
    print(f"| 1. {"Estatísticas de manchas solares":<{size-4}}|")
    print(f"| 2. {"Gráficos e visualizações":<{size-4}}|")
    print(f"| 3. {"Análise de ciclos solares":<{size-4}}|")
    print("+" + "-"*size + "+")
    return
