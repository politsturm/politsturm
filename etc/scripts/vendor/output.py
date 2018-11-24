# coding=utf-8


class color:
    def __init__(self):
        pass

    ORANGE = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def message_warning(message):
    """Предупреждение"""
    print color.ORANGE, message, color.RESET


def message_info(message):
    """Информация"""
    print color.BOLD, message, color.RESET


def message_success(message):
    """Успешно"""
    print color.GREEN, message, color.RESET