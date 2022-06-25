class IncorrectPlaceException(Exception):
    """An exception for incorrect place cmd"""

    #: The exit code for this exception.
    exit_code = 1

    def __init__(self) -> None:
        super().__init__()
        self.message = 'Incorrect place command'

    def __repr__(self) -> str:
        return self.message

    def __str__(self) -> str:
        return self.message


class IncorrectCoordinateCommand(Exception):
    """An exception for coordinate out of range cmd"""

    #: The exit code for this exception.
    exit_code = 1

    def __init__(self) -> None:
        super().__init__()
        self.message = 'coordinate out of range'

    def __repr__(self) -> str:
        return self.message

    def __str__(self) -> str:
        return self.message
