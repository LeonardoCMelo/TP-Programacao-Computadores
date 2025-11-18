from menu import main_menu
from data_read import *
from pathlib import Path

def main():
    """
    Função principal do programa.
    
    Returns:
        None
    """

    file_path = Path("data/raw/SN_m_tot_V2.0.txt")
    monthly_data = read_monthly_data(file_path)
    
    file_path = Path("data/raw/SN_d_tot_V2.0.txt")
    daily_data = read_daily_data(file_path)
    
    main_menu(monthly_data, daily_data)
    return

if __name__ == "__main__":
    main()
