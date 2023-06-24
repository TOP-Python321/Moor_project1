import data
import utils


def get_help() -> None:
    """
    Displays the 'help' section.
    """
    print(utils.show_title(data.HELP_TITLE))
    # ИСПРАВИТЬ: может, всё же прочитать файл один раз заранее, а не во время каждого вызова функции?)
    with open(data.HELP_PATH, 'r', encoding='utf-8') as f:
        file = f.read()
    print(file)

