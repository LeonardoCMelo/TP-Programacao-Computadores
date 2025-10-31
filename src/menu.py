
def main_menu():
    show_main_menu()
    main_menu_selection()

def show_main_menu():
    """
    Função para mostrar o menu principal
    """
    size: int = 40 # largura maxima
    print("+" + "-"*size + "+")
    print("|" + " Menu principal ".center(size) + "|")
    print("+" + "-"*size + "+")
    options = [
        "Estatísticas de manchas solares",
        "Gráficos e visualizações",
        "Análise de ciclos solares",
    ]
    for i in range(len(options)):
        print(f"| {i+1}. {options[i]:<{size-4}}|")
    print("+" + "-"*size + "+")
    return

def main_menu_selection():
    """
    Função para selecionar a opção certa do Menu Principal
    """
    selecting = True

    while selecting:
        try:
            select = int(input("Sua opção: "))

            if select < 1 or select > 3:
                raise ValueError
            
            selecting = False  
        except ValueError:
            print("Por favor digite um número de 1 a 3!")

    if select == 1:
        pass
    elif select == 2:
        pass
    elif select == 3:
        pass
    return
