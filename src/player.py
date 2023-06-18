import data
import utils


def name_input() -> str:
    while True:
        name = input(f'{data.MESSAGES["ввод имени"]} > ')
        if data.PATTERN.fullmatch(name):
            return name
        print(f'{data.MESSAGES["некорректное имя"]}')


def get_player_name() -> None:
    name = name_input()
    if name not in data.player_db:
        data.player_db[name] = {'побед': 0, 'поражений': 0, 'ничьих': 0}
        utils.write_player()
    data.players += [name]