from datetime import datetime, timedelta

def calculate_age(birthdate):
    '''

    :param birthdate:
    :return:
    '''
    today = datetime.now().date()

    day = today.day - birthdate.day
    month = today.month - birthdate.month
    age = today.year - birthdate.year

    if day < 0:
        month -= 1
        day += (today.replace(day=1) - timedelta(days=1)).day

    if month < 0:
        age -= 1
        month += 12

    if birthdate.month == 2 and birthdate.day == 29:
        try:
            leap_year_birthday = birthdate.replace(year=today.year)
        except ValueError:
            leap_year_birthday = birthdate.replace(year=today.year, day=28)

        if today < leap_year_birthday:
            age -= 1
    print(f"Тебе:, {age} лет, {month} месяцев, {day} дней")


while True:
    birthdate = input("Введи дату свое рождения в формате ДД ММ ГГГГ: ")
    try:
        birthdate = datetime.strptime(birthdate, "%d %m %Y").date()
        today = datetime.now().date()
        if today.year > birthdate.year:
            break
        else:
            print("Ошибка: неверный формат даты. Введите дату в формате ДД ММ ГГГГ.")
    except ValueError:
       print("Ошибка: неверный формат даты. Введите дату в формате ДД ММ ГГГГ.")


calculate_age(birthdate)
