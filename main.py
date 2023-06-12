from typing import Tuple, Set, Any


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

    for col in range(dim):
        combination = set(range(col, dim * dim, dim))
        combinations.append(combination)

    combination = set(range(0, dim * dim, dim + 1))
    combinations.append(combination)

    combination = set(range(dim - 1, dim * dim - dim + 1, dim - 1))
    combinations.append(combination)

    return tuple(combinations)


def game_field(dim: int) -> str:
    """
    Function generates the playing field
    :param dim: Int. Size of game field.
    :return: Str. return to stdout the playing field in string representation.
    """
    separator = '-' * (dim ** 2 + 5)
    cell = ' {} |' * dim
    field = ''

    for i in range(dim):
        field += f"{cell.rstrip('|')}\n{separator}\n"

    return field[:-len(separator)-1]
