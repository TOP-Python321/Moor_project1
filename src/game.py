from shutil import get_terminal_size

import bot
import data
import player
import utils


def get_human_turn() -> int | None:
    """Requests user input for a move during gameplay. If the input is incorrect, it repeats the request until the correct input is received."""
    while True:
        turn = input(data.PROMPT)
        if not turn:
            return None
        try:
            turn = int(turn)
        except ValueError:
            pass
        else:
            if 0 <= turn < data.all_cells:
                if turn not in data.turns:
                    return turn


def game():
    """
    Game process controller
    """
    # 9. Цикл до максимального количества ходов
    for t in range(len(data.turns), data.all_cells):
        o = t % 2

        ...

        # 10. Запрос хода игрока
        print(f'Ход игрока {data.players[o]} ')
        turn = get_human_turn()

        # а) ЕСЛИ ввод пустой:
        if turn is None:
            # сохранение незавершённой партии
            # СДЕЛАТЬ: сохранение игры — это сфера ответственности другой функции — вынесите этот код в отдельную функцию
            # не доделано
            utils.write_saves()
            # переход к этапу 4
            return None
        # ИСПРАВИТЬ: разве функция get_human_turn() может вернуть ещё что-то кроме int и None?
        data.turns[turn] = data.TOKENS[o]
        if set(data.turns) in utils.winning_combinations(data.dim):
            player.update_stats(data.players)
            # СДЕЛАТЬ: аналогично: работа с файлами данных вне сферы ответственности функции game()
            # with open(data.PLAYERS_PATH, 'w', encoding='utf-8') as file:
            #     file.write(data.players_db)
            utils.write_player()

    else:
        # ничья
        return []


def load(players: tuple[str, str], save: dict) -> None:
    """"""
    data.players = list(players)
    data.turns = save['turns']
    utils.change_dim(save['dim'])


def save() -> None:
    """"""
    data.saves_db |= {
        tuple(data.players): {
            'dim': data.dim,
            'turns': data.turns
        }
    }


def print_board(right: bool = False) -> None:
    """"""
    board = data.field.format(*(data.board | data.turns).values())
    if data.DEBUG:
        matr = bot.vectorization(data.debug_data.get('result'))
        cw = max(len(str(n)) for n in matr)
        matr = utils.field_template(cw).format(*matr)
        board = utils.concatenate_rows(board, matr)

    if right:
        terminal_width = get_terminal_size()[0] - 1
        margin = terminal_width - max(len(line) for line in board.split())
        margin = '\n'.join(' '*margin for _ in board.split())
        board = utils.concatenate_rows(margin, board)

    print(board)


def clear() -> None:
    """"""
    # noinspection PyTypeChecker
    data.saves_db.pop(tuple(data.players), None)
    data.players = [data.authorized]
    data.turns = {}