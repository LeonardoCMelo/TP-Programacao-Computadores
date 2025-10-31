def print_header(title: str, size: int = 40):
    """
    Print do cabeçalho do menu.

    title: Título do menu.

    size: Largura máxima do menu.
    """
    print("+" + "-"*size + "+")
    print("|" + f" {title} ".center(size) + "|")
    print("+" + "-"*size + "+")
    return

def main_menu():
    """Acoplamento para as funções do menu principal"""

    isRunning = True

    while isRunning:
        show_main_menu()
        select = main_menu_selection()

        if select == 0:
            print("Encerrando programa...")
            isRunning = False
        elif select == 1:
            statistics_menu()
        elif select == 2:
            pass
        elif select == 3:
            pass
    return

def show_main_menu():
    """
    Função para printar o menu principal
    """
    size: int = 40 # largura maxima
    print_header("Menu principal", size)
    options = [
        "Sair",
        "Estatísticas de manchas solares",
        "Gráficos e visualizações",
        "Análise de ciclos solares",
    ]
    for i, option in enumerate(options):
        print(f"| {i}. {option:<{size-4}}|")
    print("+" + "-"*size + "+")
    return

def main_menu_selection() -> int:
    """
    Função para selecionar as opções do Menu Principal.

    Retorno: Opção selecionada.
    """
    isSelecting = True

    while isSelecting:
        try:
            option = int(input("Sua opção: "))

            if option not in range(0,4):
                raise ValueError
            
            isSelecting = False  
        except ValueError:
            print("Por favor digite um número de 0 a 3!")
    
    return option

def statistics_menu():
    """Acoplamento e loop do menu de estatísticas."""
    option = -1
    while option != 0:
        show_statistics_menu()
        option = statistics_menu_selection()

        if option == 0:
            print("Voltando ao Menu Principal...\n")
        elif option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
    return

def show_statistics_menu():
    """
    Função para printar o menu de Estatisticas.
    """
    
    size: int = 40 # Largura máxima

    options = [
        "Voltar",
        "Dias sem manchas em um mês",
        "Mês com mais manchas em um intervalo",
        "Média mensal de manchas",
        "Desvio padrão mensal",
    ]
    print_header("Menu de Estatisticas", size)

    for i, option in enumerate(options):
        print(f"| {i}. {option:<{size-4}}|")

    print("+" + "-"*size + "+")
    return

def statistics_menu_selection() -> int:
    """
    Função para selecionar as opções do Menu de Estatisticas.

    Retorno: Opção selecionada.
    """
    isSelecting = True
    while isSelecting:
        try:
            option = int(input("Sua opção: "))

            if option not in range(5):
                raise ValueError
            
            isSelecting = False

        except ValueError:
            print("Por favor digite um número de 0 a 4!")
    return option