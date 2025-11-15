import matplotlib.pyplot as plt
from help_functions import date_to_decimal_year

def build_daily_series(daily_data: dict, startYear: int, endYear: int) -> tuple[list, list]:
    """
    Constrói séries temporais diárias de manchas solares dentro de um intervalo de anos.
    Args:
        daily_data (dict): Dados diários de manchas solares.
        startYear (int): Ano inicial do intervalo.
        endYear (int): Ano final do intervalo.
    Returns:
        tuple[list, list]: Listas de datas (anos decimais) e valores de manchas solares.
    """

    dates = []
    values = []

    for year, months in daily_data.items():
        if not (startYear <= year <= endYear):
            continue

        for month, days in months.items():
            for day, value in days.items():
                dates.append(date_to_decimal_year(year, month, day))
                values.append(value)

    return dates, values

def plot_sunspot_graph(daily_data: dict, monthly_data: dict, startYear: int, endYear: int) -> None:
    """Plota o gráfico das manchas solares diárias e mensais em um intervalo de anos.
    Args:
        daily_data (dict): Dados diários de manchas solares.
        monthly_data (dict): Dados mensais de manchas solares.
        startYear (int): Ano inicial do intervalo.
        endYear (int): Ano final do intervalo.
    Returns:
        None
    """
    
    d_dates, d_vals = build_daily_series(daily_data, startYear, endYear)

    plt.figure(figsize=(14, 7))

    plt.plot(d_dates, d_vals, color="gold", linewidth=0.5, label="Daily")

    plt.title("Análise das séries diárias, mensais e suavizadas das manchas solares")
    plt.xlabel("Tempo (anos)")
    plt.ylabel("Número de manchas solares ($S_n$)")

    plt.grid(True, linestyle=":", alpha=0.6)

    plt.legend()
    plt.tight_layout()
    plt.show()
    return
