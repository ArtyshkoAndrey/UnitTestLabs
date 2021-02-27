from datetime import datetime


def lab1(day: int, month: int, day1: int, month1: int, year1: int):
    try:
        format_date = "%Y-%m-%d"
        birth_date = datetime.strptime(str(year1) + '-' + str(month) + '-' + str(day), format_date)
        date = datetime.strptime(str(year1) + '-' + str(month1) + '-' + str(day1), format_date)
        diff = date - birth_date
        answer = int(diff.days)
        answer = answer * (-1)

        # Если день рождение прошло
        if answer < 0:
            base = datetime.strptime(str(year1 + 1) + '-' + str(month) + '-' + str(day), format_date)
            diff = base - date
            answer = int(diff.days)

        return answer
    # Если ошибка в воде данных
    except ValueError as e:
        return None
