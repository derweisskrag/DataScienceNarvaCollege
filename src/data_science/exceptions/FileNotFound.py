error_msg = f"File specified was not found at"


class FileNotFound(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)