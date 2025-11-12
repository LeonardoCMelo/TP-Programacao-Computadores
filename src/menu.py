from spot_analysis import *
from help_functions import *

# Criador de menus
def show_menu(title: str, options: list, size: int):
    """
    Imprime um menu com o cabeçalho e as opções.

    Args:
        title (str): Título do menu
        options (list): Lista de opções do menu
        size (int): Largura do menu
    """
    print_header(title, size)
    for i, option in enumerate(options):
        print(f"| {i}. {option:<{size-4}}|")
    print("+" + "-"*size + "+")
    return

def menu_selection(option_quant: int) -> int:
    """
    Função para selecionar as opções dos menus.
    
    Args:
        option_quant(int): quantidade de opções do menu.

    Returns: 
        Opção selecionada.
    """
    isSelecting = True

    while isSelecting:
        try:
            option = int(input("Sua opção: "))

            if option not in range(0,option_quant+1):
                raise ValueError
            
            isSelecting = False  
        except ValueError:
            print(f"Por favor digite um número de 0 a {option_quant}!")
    
    return option

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
    """
    Acoplamento para as funções do menu principal

    Args:
        monthly_data (dict): Dados mensais
        daily_data (dict): Dados diários
    """
    options = [
        "Sair",
        "Estatísticas de manchas solares",
        "Gráficos e visualizações",
        "Análise de ciclos solares",
    ]

    isRunning = True

    while isRunning:
        show_menu("Menu Principal", options, 40)
        #show_main_menu()
        select = menu_selection(len(options)-1)

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

# Menu de estatisticas
def statistics_menu(monthly_data: dict, daily_data: dict):
    """Acoplamento para as funções do menu de estatísticas."""

    options = [
        "Voltar",
        "Dias sem manchas em um ano",
        "Ano e mês com mais dias sem manchas em um intervalo",
        "Ano e mês com mais manchas em um intervalo",
        "Máximo e mínimo de manchas em um intervalo",
        "Média mensal de manchas",
        "Desvio padrão mensal",
    ]

    option = -1
    while option != 0:
        show_menu("Menu de Estatisticas", options, 60)
        option = menu_selection(len(options)-1)

        if option == 0:
            print("Voltando ao Menu Principal...\n")
        elif option == 1:
            year = int(input("Digite o ano: "))
            result = count_days_without_spot(daily_data, year)
            print(f"Dias sem manchas em cada mês de {year}:")
            for i, dias in enumerate(result, start=1):
                if dias is not None:
                    print(f"Mês {i:02d}: {dias} dias sem manchas")
                else:
                    print(f"Mês {i:02d}: sem dados")
        elif option == 2:
            date1 = input("Digite a primeira data no formato dd/mm/yyyy : ")
            date2 = input("Digite a segunda data no formato dd/mm/yyyy : ")
            result = year_month_without_sunspots(daily_data, date1, date2)
            if None in result:
                print()
            else:
                print(f"Entre {date1} e {date2} o mes que teve mais dias sem manchas solares foi {month_int2str(result[0])} de {result[1]}")
        elif option == 3:
            date1 = input("Digite a primeira data no formato dd/mm/yyyy : ")
            date2 = input("Digite a segunda data no formato dd/mm/yyyy : ")
            result = year_month_most_sunspots(daily_data, date1, date2)
            if None in result:
                print()
            else:
                print(f"Entre {date1} e {date2} o mes que teve mais manchas solares foi {month_int2str(result[0])} de {result[1]}")
        elif option == 4:
            date1 = input("Digite a primeira data no formato dd/mm/yyyy : ")
            date2 = input("Digite a segunda data no formato dd/mm/yyyy : ")
            result = max_min_sunspots(daily_data, date1, date2)
            if None in result:
                print()
            else:
                print(f"Entre as datas de {date1} e {date2}:")
                print(f"Valor máximo de manchas solares: {result[0]}")
                print(f"Valor mínimo de manchas solares: {result[1]}")
    return