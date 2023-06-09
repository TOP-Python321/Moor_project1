"""
Точка входа
"""

# ИСПОЛЬЗОВАТЬ: документация модуля, как и документация функции, размещается в самом начале тела — потом уже импорты
import data
import game
import help
import player
import utils


print(utils.show_title("КРЕСТИКИ-НОЛИКИ"))
# Чтение файлов

# Если первый запуск:
    # Вывод раздела помощи
if not utils.read_players():
    utils.read_saves()
    help.get_help()

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
        help.get_help()
    elif command in data.COMMANDS['создать или переключиться на игрока']:
        pass
    elif command in data.COMMANDS['отобразить таблицу результатов']:
        pass
    elif command in data.COMMANDS['изменить размер поля']:
        pass
    elif command in data.COMMANDS['выйти']:
        break

