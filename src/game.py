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
            players = ','.join(person for person in data.players)
            turns = tuple(turn[0] for turn in data.turns.items())
            save = f'\n{players}!{turns}!{data.dim}'
            with open(data.SAVES_PATH, 'a', encoding='utf-8') as file:
                file.write(save)
            # переход к этапу 4
            return None
        # ИСПРАВИТЬ: разве функция get_human_turn() может вернуть ещё что-то кроме int и None?
        elif isinstance(turn, int):
            data.turns[turn] = data.TOKENS[o]
            if set(data.turns) in utils.winning_combinations(data.dim):
                player.update_stats(data.players)
                # СДЕЛАТЬ: аналогично: работа с файлами данных вне сферы ответственности функции game()
                with open(data.PLAYERS_PATH, 'w', encoding='utf-8') as file:
                    file.write(data.players_db)

    else:
        # ничья
        return []