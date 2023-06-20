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
    width = dim*4+1
    separator = '-'
    cell_separator = '|'
    line = f'\n{separator*width}\n'
    return line.join(
        cell_separator.join(' {} ' for _ in range(dim))
        for _ in range(dim)
    )


# Пока не придумал, как не выводить последнюю подстроку с ----
# Также, не учтена ширина разделяющей полосы и выравнивание в ячейках.
# При размере игрового поля 3х3 все нормально, но, если сделать его 4х4, то нужно учитывать количество пробелов в
# ячейках от 0 до 9.


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


def write_player() -> None:
    """
    Writes information from the corresponding global data structure to the player data file.
    """
    config = ConfigParser()
    config.read_dict(data.players_db)
    with open(data.PLAYERS_PATH, 'a', encoding='utf-8') as file:
        config.write(file)


# Не закончена
def get_commands() -> str:
    """
    Prints commands.
    """
    commands = ''
    for desc, title in data.COMMANDS.items():
        commands += f'{title} - {desc}\n'
    return commands
