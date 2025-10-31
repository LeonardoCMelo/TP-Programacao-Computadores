def read_monthly_data(file_path: str) -> dict:
    """
    Lê os dados mensais de manchas solares e organiza em um dicionário hierárquico.

    Estrutura retornada:
    {
        ano: {
            mês: {
                "decimal_date": float,
                "month_avg": float,
                "std_deviation": float,
                "num_obs": int
            },
            ...
        },
        ...
    }

    Parâmetros:
        file_path (str): Caminho para o arquivo de dados mensais (ex: SN_m_tot_V2.0.txt)

    Retorna:
        dict: Dicionário organizado por ano e mês.
    """
    data = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() == "" or line.startswith("#"):
                continue

            parts = line.split()

            year = int(parts[0])
            month = int(parts[1])
            decimal_date = float(parts[2])
            month_avg = float(parts[3])
            std_dev = float(parts[4])
            num_obs = int(parts[5])

            if year not in data:
                data[year] = {}
            
            data[year][month] = {
                "decimal_date": decimal_date,
                "month_avg": month_avg,
                "std_deviation": std_dev,
                "num_obs": num_obs,
            }
    return data

def read_daily_data(file_path: str) -> dict:
    """
    Lê os dados diários de manchas solares e organiza em um dicionário hierárquico.

    Estrutura retornada:
    {
        ano: {
            mês: {
                dia: {
                    "decimal_date": float,
                    "daily_sunspot": int,
                    "std_deviation": float,
                    "num_obs": int
                }
            }
        }
    }

    Parâmetros:
        file_path (str): Caminho para o arquivo de dados diários (ex: SN_d_tot_V2.0.txt)

    Retorna:
        dict: Dicionário organizado por ano, mês e dia.
    """
    data = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() == "" or line.startswith("#"):
                continue

            parts = line.split()

            year = int(parts[0])
            month = int(parts[1])
            day = int(parts[2])
            decimal_date = float(parts[3])
            daily_sunspot = int(parts[4])
            std_dev = float(parts[5])
            num_obs = int(parts[6])

            if year not in data:
                data[year] = {}
            
            if month not in data[year]:
                data[year][month] = {}
            
            data[year][month][day] = {
                "decimal_date": decimal_date,
                "daily_sunspot": daily_sunspot,
                "std_deviation": std_dev,
                "num_obs": num_obs,
            }
    return data