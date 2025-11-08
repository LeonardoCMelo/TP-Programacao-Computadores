def read_monthly_data(file_path: str) -> dict:
    data = {}
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip() == "" or line.startswith("#"):
                    continue

                parts = line.split()

                year = int(parts[0])
                month = int(parts[1])
                month_avg = float(parts[3])
                std_dev = float(parts[4])

                if month_avg < 0:
                    month_avg = None

                if year not in data:
                    data[year] = {}
                
                data[year][month] = {
                    "month_avg": month_avg,
                    "std_deviation": std_dev,
                }
    except FileNotFoundError:
        print(f"O arquivo '{file_path}' não foi encontrado. Verifique se foi salvo conforme as instruções no Notebook.")
    return data

def read_daily_data(file_path: str) -> dict:

    data = {}
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip() or line.startswith("#"):
                    continue

                parts = line.split()

                year = int(parts[0])
                month = int(parts[1])
                day = int(parts[2])
                daily_sunspot = int(parts[4])
                
                if daily_sunspot < 0:
                    daily_sunspot = None

                if year not in data:
                    data[year] = {}
                
                if month not in data[year]:
                    data[year][month] = {}
                
                data[year][month][day] = {
                    "daily_sunspot": daily_sunspot,
                }
    except FileNotFoundError:
        print(f"O arquivo '{file_path}' não foi encontrado. Verifique se foi salvo conforme as instruções no Notebook.")
    return data
