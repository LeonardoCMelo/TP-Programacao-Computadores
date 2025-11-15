def date_str2int(date: str) -> tuple[int, int, int] | tuple[None, None, None]:
    """
    Converte uma string de data no formato "dd/mm/aaaa" para uma tupla
    de inteiros (dia, mês, ano).

    Args:
        date (str): Data no formato "dd/mm/aaaa".

    Returns:
        tuple[int, int, int]: Tupla contendo (dia, mês, ano) como inteiros.
        tuple[None, None, None]: Se o formato da data for inválido.
    """
    try:
        parts = map(int, date.split('/'))
        parts = tuple(parts)

        if len(parts) != 3:
            raise ValueError
        
        d, m, y = map(int, parts)

        if not (d <= 31 and 1 <= m <= 12 and 1000 <= y <= 9999):
            raise ValueError
        
        return d, m, y
    except ValueError:
        print(f"⚠️ Formato de data inválido: '{date}'. Use o formato dd/mm/aaaa.")
        return None, None, None

def month_int2str(month: int):
    """
    Converte um número de mês (1-12) para o nome do mês correspondente em português.
    Args:
        month (int): Número do mês (1-12).
    Returns:
        str: Nome do mês em português.
    """
    meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
    return meses[month-1]

def date_to_decimal_year(year: int, month: int, day: int = 15) -> float:
    """
    Converte uma data para o formato de ano decimal.
    
    Args:
        year (int): Ano.
        month (int): Mês.
        day (int, optional): Dia. Padrão é 15.
    
    Returns:
        float: Ano em formato decimal.
    """
    
    return year + (month - 1)/12 + (day - 1)/365

def get_year_range(data: dict) -> tuple[int, int]:
    """
    Retorna o ano mínimo e máximo presente nos dados fornecidos.
    
    Args:
        data (dict): Dados de manchas solares organizados por ano.
    
    Returns:
        tuple[int, int]: Ano mínimo e máximo.
    
    """
    years = list(data.keys())
    return min(years), max(years)
