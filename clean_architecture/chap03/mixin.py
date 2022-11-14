from typing import Generator


class BaseTokenizer:
    def __init__(self, str_token: str) -> None:
        self.str_token = str_token

    def __iter__(self) -> Generator[str, None, None]:
        yield from self.str_token.split("-")


class UpperIterableMixin:
    def __iter__(self) -> Generator[str, None, None]:
        yield from map(str.upper, super().__iter__())


class Tokenizer(UpperIterableMixin, BaseTokenizer):
    pass


if __name__ == "__main__":
    str_token = "234g-4hd2-fg23-b45f"

    print(">> BaseTokenizer")
    tk = BaseTokenizer(str_token)
    print(list(tk))

    print("\n>> MixinTokenizer")
    tk = Tokenizer(str_token)
    print(list(tk))