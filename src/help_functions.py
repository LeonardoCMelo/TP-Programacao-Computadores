def date_str2int(date: str) -> tuple[int, int, int] | tuple[None, None, None]:
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
    meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
    return meses[month-1]
