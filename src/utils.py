from configparser import ConfigParser
from shutil import get_terminal_size
from typing import Tuple, Set, Any

import data


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


def field_template(dim: int) -> str:
    """
    Function generates the playing field
    :param dim: Int. Size of game field.
    :return: Str. return to stdout the playing field in string representation.
    """
    # ИСПРАВИТЬ: dim*3 + (dim-1) => dim*4 - 1
    width = dim*4+1
    separator = '-'
    cell_separator = '|'
    line = f'\n{separator*width}\n'
    return line.join(
        # ИСПРАВИТЬ: эту строку тоже можно сгенерировать один раз заранее
        cell_separator.join(' {} ' for _ in range(dim))
        for _ in range(dim)
    )


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
