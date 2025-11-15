from help_functions import date_str2int

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

    if None in (m1, y1, m2, y2):
        return None, None

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
    return best_month, best_year

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

    if None in (d1, m1, y1, d2, m2, y2):
        return None, None

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

    return best_month, best_year

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

    if None in (d1, m1, y1, d2, m2, y2):
        return None, None
    
    for year in range(y1, y2 + 1):
        first_month = m1 if year == y1 else 1
        last_month = m2 if year == y2 else 12
        for month in range(first_month, last_month + 1):
            for day in daily_data[year][month]:
                value = daily_data[year][month][day]
                if max_sunspot == None or value>max_sunspot:
                    max_sunspot = value
                elif min_sunspot == None or value<min_sunspot:
                    min_sunspot = value
    return max_sunspot, min_sunspot
