def count_days_without_spot(daily_data: dict[int, dict[int, dict[int, dict[str, float]]]], year: int) -> list:
    result = []
    for month in range(1, 13):
        if year in daily_data and month in daily_data[year]:
            dias_sem_manchas = sum(
                1 
                for valores in daily_data[year][month].values()
                if valores["daily_sunspot"] in (0, None)
            )
            result.append(dias_sem_manchas)
        else:
            result.append(None)
    return result
