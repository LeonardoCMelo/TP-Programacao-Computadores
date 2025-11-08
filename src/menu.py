from spot_analysis import *
from help_functions import *

# Criação de cabecalho
def print_header(title: str, size: int = 42):
    """
    Print do cabeçalho do menu.

    title: Título do menu.

    size: Largura máxima do menu.
    """
    print("+" + "-"*size + "+")
    print("|" + f" {title} ".center(size) + "|")
    print("+" + "-"*size + "+")
    return

# Menu Principal
def main_menu(monthly_data: dict, daily_data: dict):
    """Acoplamento para as funções do menu principal"""

    isRunning = True

    while isRunning:
        show_main_menu()
        select = main_menu_selection()

        if select == 0:
            print("Encerrando programa...")
            isRunning = False
        elif select == 1:
            statistics_menu(monthly_data, daily_data)
        elif select == 2:
            pass
        elif select == 3:
            pass
    return

def show_main_menu():
    """
    Função para printar o menu principal
    """
    size: int = 42 # largura maxima
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

# Menu de estatisticas
def statistics_menu(monthly_data: dict, daily_data: dict):
    """Acoplamento e loop do menu de estatísticas."""
    option = -1
    while option != 0:
        show_statistics_menu()
        option = statistics_menu_selection()

        if option == 0:
            print("Voltando ao Menu Principal...\n")
        elif option == 1:
            year = int(input("Digite o ano: "))
            result = count_days_without_spot(daily_data, year)
            print(f"Dias sem manchas em cada mês de {year}:")
            for i, dias in enumerate(result, start=1):
                if dias is not None:
                    print(f"  Mês {i:02d}: {dias} dias sem manchas")
                else:
                    print(f"  Mês {i:02d}: sem dados")
        elif option == 2:
            date1 = input("Digite a primeira data no formato dd/mm/yyyy : ")
            date2 = input("Digite a segunda data no formato dd/mm/yyyy : ")
            result = year_month_without_sunspots(daily_data, date1, date2)
            if None in result:
                print()
            else:
                print(f"Entre {date1} e {date2} o mes que teve mais dias sem manchas solares foi {month_int2str(result[0])} de {result[1]}")
        elif option == 3:
            pass
        elif option == 4:
            pass
    return

def show_statistics_menu():
    """
    Função para printar o menu de Estatisticas.
    """
    
    size: int = 60 # Largura máxima

    options = [
        "Voltar",
        "Dias sem manchas em um ano",
        "Ano e mês com mais dias sem manchas em um intervalo",
        "Ano e mês com mais manchas em um intervalo",
        "Máximo e mínimo de manchas em um intervalo",
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
