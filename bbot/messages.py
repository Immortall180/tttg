MESSAGES = {
    'weather_for_location_retrieval_failed': 'Провертье название города ,',

    'general_failure': 'Данная команда не существует.\n\n /help - инструкция по использованию бота.',

    'weather_in_city_message': 'Погода в  городе {}:\n{}\nтемпература: {:.1f}°C.',

    'weather_in_location_message': 'Погода в указанной локации:\n{}\nтемпература: {:.1f}°C.',

    'help': 'Проверьте название города',
    'start': 'Просто напишите название города и я вам напишу какая сейчас там погода'
}


def get_message(message_key: str):
    return MESSAGES[message_key]
