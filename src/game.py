from configparser import ConfigParser
import data
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
        if isinstance(turn, int):
            data.turns[turn] = data.TOKENS[o]

        # а) ЕСЛИ ввод пустой:
        if turn is None:
            # сохранение незавершённой партии
            # не доделано
            data.saves_db[data.players] = data.turns
            config = ConfigParser()
            for elem in data.saves_db:
                config[','.join(elem)] = {data.players.join([str(i) for i in data.saves_db[elem]])}
            with open(data.SAVES_PATH, 'a', encoding='utf-8') as file:
                config.write(file)
            # переход к этапу 4
            return None

        ...

    else:
        # ничья
        return []