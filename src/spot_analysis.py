from help_functions import date_str2int
import math

def count_days_without_spot(daily_data: dict, year: int) -> list:
    """
    Conta o número de dias sem manchas solares para cada mês de um ano específico.

    Args:
        daily_data (dict): Dados diários de manchas solares.
        year (int): Ano para o qual contar os dias sem manchas.

    Returns:
        list: Lista com o número de dias sem manchas para cada mês (índices 0-11 correspondem a janeiro-dezembro).
    """
    
    result = []
    for month in range(1, 13):
        if year in daily_data and month in daily_data[year]:
            dias_sem_manchas = sum(
                1
                for value in daily_data[year][month].values()
                if value in (0, None)
            )
            result.append(dias_sem_manchas)
        else:
            result.append(None)
    return result

def year_month_without_sunspots(daily_data: dict, date1: str, date2: str) -> tuple[int, int]:
    """
    Encontra o ano e mês com o maior número de dias sem manchas solares em um intervalo de datas.

    Args:
        daily_data (dict): Dados diários de manchas solares.
        date1 (str): Data inicial no formato "dd/mm/aaaa".
        date2 (str): Data final no formato "dd/mm/aaaa".

    Returns:
        tuple[int, int]: Tupla contendo (mês, ano) com o maior número de dias sem manchas solares.
    """

    _, m1, y1 = date_str2int(date1)
    _, m2, y2 = date_str2int(date2)
    result = ()
    if None in (m1, y1, m2, y2):
        result = (None, None)
    else:
        max_wo_spots = -1
        best_year, best_month = None, None

        for year in range(y1, y2 + 1):
            for month in range(1, 13):
                if (year == y1 and month < m1) or (year == y2 and month > m2):
                    continue
                if year not in daily_data or month not in daily_data[year]:
                    continue

                days_wo_spots = sum(
                    1
                    for value in daily_data[year][month].values()
                    if value in (0, None)
                )

                if days_wo_spots > max_wo_spots:
                    max_wo_spots = days_wo_spots
                    best_month, best_year = month, year
        result = (best_month, best_year)
    return result

def year_month_most_sunspots(daily_data: dict, date1: str, date2: str) -> tuple[int, int]:
    """
    Encontra o ano e mês com o maior número de manchas solares em um intervalo de datas.
    
    Args:
        daily_data (dict): Dados diários de manchas solares.
        date1 (str): Data inicial no formato "dd/mm/aaaa".
        date2 (str): Data final no formato "dd/mm/aaaa".
    
    Returns:
        tuple[int, int]: Tupla contendo (mês, ano) com o maior número de manchas solares.
    """

    d1, m1, y1 = date_str2int(date1)
    d2, m2, y2 = date_str2int(date2)

    result = ()

    if None in (d1, m1, y1, d2, m2, y2):
        result = None, None
    else:
        max_total = -1
        best_year, best_month = None, None

        for year in range(y1, y2 + 1):
            first_month = m1 if year == y1 else 1
            last_month = m2 if year == y2 else 12

            for month in range(first_month, last_month + 1):
                if (year == y1 and month < m1) or (year == y2 and month > m2):
                    continue
                if year not in daily_data or month not in daily_data[year]:
                    continue

                total = sum(
                    value or 0
                    for value in daily_data[year][month].values()
                    if value is not None
                )

                if total > max_total:
                    max_total = total
                    best_year, best_month = year, month
        result = best_month, best_year
    return result

def max_min_sunspots(daily_data: dict[dict[dict[int]]], date1: str, date2: str) -> tuple[int, int]:
    """
    Encontra o valor máximo e mínimo de manchas solares em um intervalo de datas.

    Args:
        daily_data (dict): Dados diários de manchas solares.
        date1 (str): Data inicial no formato "dd/mm/aaaa".
        date2 (str): Data final no formato "dd/mm/aaaa".

    Returns:
        tuple[int, int]: Tupla contendo (máximo, mínimo) de manchas solares.
    """

    max_sunspot = None
    min_sunspot = None

    d1, m1, y1 = date_str2int(date1)
    d2, m2, y2 = date_str2int(date2)

    result = ()

    if None in (d1, m1, y1, d2, m2, y2):
        result = None, None
    else:
        for year in range(y1, y2 + 1):
            first_month = m1 if year == y1 else 1
            last_month = m2 if year == y2 else 12
            for month in range(first_month, last_month + 1):
                for day in daily_data[year][month]:
                    value = daily_data[year][month][day]

                    if value is None:
                        continue

                    if max_sunspot == None or value > max_sunspot:
                        max_sunspot = value

                    if min_sunspot == None or value < min_sunspot:
                        min_sunspot = value
        result = max_sunspot, min_sunspot
    return result

def monthly_std_dev(daily_data: dict, year: int, month: int) -> float:
    """
    Calcula o desvio padrão mensal das manchas solares para um mês e ano específicos.
    Args:
        daily_data (dict): Dados diários de manchas solares.
        year (int): Ano específico.
        month (int): Mês específico.
    
    Returns:
        float: Desvio padrão das manchas solares para o mês especificado.
    """
    
    if year not in daily_data or month not in daily_data[year]:
        result = None
    else:
        values = list(daily_data[year][month].values())
        n = len(values)

        if n < 2:
            return None

        avg = sum(values) / n
        square_sum = sum((v - avg) ** 2 for v in values)

        std_dev = math.sqrt(square_sum / (n - 1))
        
        result = std_dev

    return result

def monthly_avg(daily_data: dict, year: int) -> tuple:
    """
    Calcula a média mensal de manchas solares para cada mês de um ano específico.
    Args:
        daily_data (dict): Dados diários de manchas solares.
        year (int): Ano específico.
    
    Returns:
        tuple: Tupla contendo a média mensal de manchas solares para cada mês (índices 0-11 correspondem a janeiro-dezembro).
    """
    result = []
    for month in range(1, 13):
        if year in daily_data and month in daily_data[year]:
            values = [
                value
                for value in daily_data[year][month].values()
                if value is not None
            ]
            if values:
                avg = sum(values) / len(values)
                result.append(avg)
            else:
                result.append(None)
        else:
            result.append(None)
    result = tuple(result)
    return result