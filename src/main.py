from menu import main_menu
from data_read import *

def main():
    monthly_data = read_monthly_data("D:\\Users\\leona\\Documents\\UFMG\\2025_2\\PC\\TP-Programacao-Computadores\\data\\raw\\SN_m_tot_V2.0.txt")
    daily_data = read_daily_data("D:\\Users\\leona\\Documents\\UFMG\\2025_2\\PC\\TP-Programacao-Computadores\\data\\raw\\SN_d_tot_V2.0.txt")
    main_menu()
    return

if __name__ == "__main__":
    main()