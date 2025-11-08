from help_functions import date_str2int

def count_days_without_spot(daily_data: dict, year: int) -> list:
    result = []
    for month in range(1, 13):
        if year in daily_data and month in daily_data[year]:
            dias_sem_manchas = sum(
                1 
                for values in daily_data[year][month].values()
                if values["daily_sunspot"] in (0, None)
            )
            result.append(dias_sem_manchas)
        else:
            result.append(None)
    return result

def year_month_without_sunspots(daily_data: dict, date1: str, date2: str) -> tuple[int, int]:
    _, m1, y1 = date_str2int(date1)
    _, m2, y2 = date_str2int(date2)

    if None in (m1, y1, m2, y2):
        return None, None

    max_wo_spots = -1
    best_year, best_month = None, None
    
    for year in range(y1, y2+1):
        for month in range(1,13):
            if (year == y1 and month < m1) or (year == y2 and month > m2):
                continue
            if month not in daily_data[year]:
                continue

            days_wo_spots = sum(
                1
                for _, values in daily_data[year][month].items()
                if values.get("daily_sunspot") in (0, None)
            )

            if days_wo_spots > max_wo_spots:
                max_wo_spots = days_wo_spots
                best_month, best_year = month, year
    return best_month, best_year
