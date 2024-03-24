from weather import WeatherInfo


temperature_rules = [
    (-20, 'Очень холодно, одевайте самые теплые вещи'),
    (-10, 'Достаточно холодно, одевайтесь теплее.'),
    (0, 'Холодно, оденьте куртку.'),
    (10, 'Прохладно,легкая куртка не помешает.'),
    (15, 'Приятная погода, ветровка самое то .'),
    (20, 'Тепло. Легкая кофта подойдет.'),
    (27, 'Жарко, оденьтесь легко.'),
    (40, 'Очень жарко, пейте больше воды.'),

]


def get_temperature_advice(temperature: int) -> str:
    for rule, advice in temperature_rules:
        if temperature < rule:
            return advice

    return ''


def get_status_advice(weather: str) -> str:
    if 'дожд' in weather:
        return 'Возьмите зонтик.'
    return ''


def get_advice(weather: WeatherInfo) -> str:
    advice = get_temperature_advice(weather.temperature)
    advice += '\n'
    advice += get_status_advice(weather.status)
    return advice
