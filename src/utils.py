from configparser import ConfigParser
from shutil import get_terminal_size
from typing import Tuple, Set, Any

import data
import game


def winning_combinations(dim: int) -> Tuple[Set[Any], ...]:
    """
    The function generates a tuple with sets of winning combinations
    :param dim: Int. Size of game field.
    :return: Tuple.
    """
    combinations = []

    for row in range(dim):
        combination = set(range(row * dim, (row + 1) * dim))
        combinations.append(combination)
        combination = set(range(row, dim * dim, dim))
        combinations.append(combination)

    combination = set(range(0, dim * dim, dim + 1))
    combinations.append(combination)

    combination = set(range(dim - 1, dim * dim - dim + 1, dim - 1))
    combinations.append(combination)

    return tuple(combinations)


def field_template(data_width: int = None) -> str:
    """
    Function generates the playing field
    :param dim: Int. Size of game field.
    :return: Str. return to stdout the playing field in string representation.
    """
    # ИСПРАВИТЬ: dim*3 + (dim-1) => dim*4 - 1
    if data_width is None:
        field_width = data.dim * (3 + max(len(t) for t in data.TOKENS)) - 1
    else:
        field_width = data.dim * (3 + data_width) - 1
    v_sep, h_sep = '|', '—'
    v_sep = v_sep.join([' {} '] * data.dim)
    h_sep = f'\n{h_sep * field_width}\n'
    return h_sep.join([v_sep] * data.dim)
        # ИСПРАВИТЬ: эту строку тоже можно сгенерировать один раз заранее


def show_title(text: str) -> str:
    """
    Function generates a string in which the passed text will be framed by the characters '=' and '#'
    :param text: String. Title message.
    :return: String.
    """
    terminal_size = get_terminal_size().columns - 3
    text_rows = []
    row = ''
    lines = '#' + '=' * terminal_size + '#\n'
    empty_line = f"#{' ' * terminal_size}#\n"

    for word in text.split():
        if len(row + word) > terminal_size - 4:
            text_rows += f'#{row.center(terminal_size)}#\n'
            row = ''
        row += f'{word} '
    text_rows += f'#{row.center(terminal_size)}#\n'

    header = lines + empty_line + ''.join(text_rows) + empty_line + lines

    return header


def read_players() -> bool:
    """
    Reads a player data file, saves the information to the appropriate global data structure. Returns True if there is at least one entry in the player data file, False otherwise.
    """
    config = ConfigParser()
    config.read(data.PLAYERS_PATH)
    config = {
        player_name: {
            key: int(value)
            for key, value in config[player_name].items()
        }
        for player_name in config.sections()
    }
    data.player_db = config
    return bool(config)


def read_saves() -> None:
    """"""
    saves = data.SAVES_PATH.read_text(encoding='utf-8').split('\n')
    for save in saves:
        players, turns, dim = save.split('!')
        data.saves_db |= {
            tuple(players.split(',')): {
                'dim': int(dim),
                'turns': {
                    int(turn): data.TOKENS[i%2]
                    for i, turn in enumerate(turns.split(','))
                },
            }
        }


def load_saves() -> dict:
    """Returns a dictionary with saves for the current player"""
    slots = {}
    index = 1
    if data.saves_db:
        for players, turns in data.saves_db.items():
            if data.players[0] in players:
                slots[index] = players, turns['turns']
                index += 1
        return slots


def get_saves(saves) -> int:
    """Requests and returns the saved game number"""
    if saves:
        print("\nДля вас доступны следующие сохранения:\n")
        for players, turns in load_saves().items():
            print(players, turns)
    else:
        return "Сохранения не найдены"
    while True:
        slot = int(input(f"Выберите сохраненную игру: "))
        if slot in saves:
            data.players = [*saves[slot][0]]
            data.turns = saves[slot][1]
            return slot


def load_game():

    index = 0
    last_turns = []
    if len(data.turns) < 2:
        print("В этой партии было сделано менее 2-х ходов")
    else:
        turns_list = list(data.turns.keys())
        last_turns = turns_list[-2:]
    for pos, token in data.turns.items():
        if pos in data.board:
            data.board[pos] = token
        if pos in last_turns:
            game.print_board()
        index = abs(index - 1)


def load():
    saves = load_saves()
    get_saves(saves)
    load_game()


def dim_input() -> int:
    while True:
        dim = input(f' {data.MESSAGES["ввод размерности"]}{data.PROMPT}')
        if data.DIM_PATTERN.fullmatch(dim):
            return int(dim)
        print(f' {data.MESSAGES["некорректная размерность"]} ')



def write_player() -> None:
    """
    Writes information from the corresponding global data structure to the player data file.
    """
    config = ConfigParser()
    config.read_dict(data.players_db)
    # ИСПРАВИТЬ: функция read_players() читает в словарь data.players_db всё содержимое файла, затем здесь вы читаете в конфиг-объект весь словарь data.players_db — следовательно вам надо файл перезаписывать, а не дозаписывать
    with open(data.PLAYERS_PATH, 'w', encoding='utf-8') as file:
        config.write(file)


def write_saves() -> None:
    """"""
    players = ','.join(person for person in data.players)
    turns = ','.join(str(turn[0]) for turn in data.turns.items())
    save_game = f'\n{players}!{turns}!{data.dim}'
    with open(data.SAVES_PATH, 'a', encoding='utf-8') as file:
        file.write(save_game)


def change_dim(new_dim: int) -> None:
    """"""
    data.dim = new_dim
    data.dim_range = range(new_dim)
    data.all_cells = new_dim**2
    data.board = dict.fromkeys(range(1, data.all_cells+1), ' ')


def concatenate_rows(
        matrix1: str,
        matrix2: str,
        *matrices: str,
        padding: int = 8
) -> str:
    """"""
    matrices = matrix1, matrix2, *matrices
    matrices = [m.split('\n') for m in matrices]
    padding = ' '*padding
    return '\n'.join(
        padding.join(row)
        for row in zip(*matrices)
    )


# Не закончена
def get_commands() -> None:
    """
    Prints commands.
    """
    commands = ''
    for desc, title in data.COMMANDS.items():
        commands += f'{title} - {desc}\n'
    print('\n\nДоступные команды:\n',commands)
