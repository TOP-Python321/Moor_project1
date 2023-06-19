import data
import player
"""
Точка входа
"""
# Чтение файлов

# Если первый запуск:
    # Вывод раздела помощи

player.get_player_name()

# Суперцикл
while True:
    # Ожидание ввода команды
    command = input('Введите команду: ')

    if command in data.COMMANDS['начать новую партию']:
        pass
    elif command in data.COMMANDS['загрузить существующую партию']:
        pass
    elif command in data.COMMANDS['отобразить раздел помощи']:
        pass
    elif command in data.COMMANDS['создать или переключиться на игрока']:
        pass
    elif command in data.COMMANDS['отобразить таблицу результатов']:
        pass
    elif command in data.COMMANDS['изменить размер поля']:
        pass
    elif command in data.COMMANDS['выйти']:
        pass

