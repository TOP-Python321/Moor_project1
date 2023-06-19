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
    if name not in data.players_db:
        data.players_db[name] = {'побед': 0, 'поражений': 0, 'ничьих': 0}
        utils.write_player()
    data.players += [name]


def update_stats(result: list[str]) -> None:
    """Updates the statistics of active players according to the results of the game."""
    if result:
        winner, looser = result
        data.players_db[winner]['побед'] += 1
        data.players_db[looser]['поражений'] += 1
    else:
        for name in data.players:
            data.players_db[name]['ничьих'] += 1