import data
import game
import player
import utils
"""
Точка входа
"""
utils.show_title("КРЕСТИКИ-НОЛИКИ")
# Чтение файлов

# Если первый запуск:
    # Вывод раздела помощи

player.get_player_name()

# Суперцикл
while True:
    # Ожидание ввода команды
    utils.get_commands()
    command = input('Введите команду: ')
    player.get_player_name()

    if command in data.COMMANDS['начать новую партию']:
        game.game()
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

