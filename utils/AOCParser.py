from collections.abc import Callable
from typing import Any


class AOCParser:

    def __init__(self, input_str: str, row_parser: Callable[[str], list | tuple | set | dict], has_header: bool = False, header_parser: Callable[[str], list | tuple | set | dict] or None = None, row_preprocessor: Callable[[list | tuple | set | dict], Any] | None = None):
        """Parser for Advent of Code input strings.
        Args:
            input_str (str): Input string to parse.
            row_parser (Callable[[str], list | tuple | set | dict]): Function to parse each row of the input string.
            has_header (bool, optional): Whether the input string has a header. Defaults to False.
            header_parser (Callable[[str], list | tuple | set | dict], optional): Function to parse the header of the input string. Defaults to None.
            row_preprocessor (Callable[[list | tuple | set | dict], Any], optional): Function to preprocess each row after parsing. Defaults to None."""
        assert isinstance(input_str, str), "Input must be a string."
        assert callable(row_parser), "Row parser must be a callable function."
        assert isinstance(has_header, bool), "has_header must be a boolean."
        assert not has_header or callable(header_parser), "Header parser must be a callable function if has_header is True."
        assert not row_preprocessor or callable(row_preprocessor), "Row preprocessor must be a callable function if provided."

        self.input: str = input_str
        self.has_header: bool = has_header
        self.row_parser: Callable[[str], list | tuple | set | dict] = row_parser
        self.header_parser: Callable[[str], list | tuple | set | dict] = header_parser
        self.row_preprocessor: Callable[[list | tuple | set | dict], Any] | None = row_preprocessor

        self.count: int = 0

        self.header: list | tuple | set | dict | None = None
        self._rows: list[list | tuple | set | dict] | None = None
        self._preprocessed_results: list | None = None

    def parse(self):
        if self.has_header:
            self.header = self.header_parser(self.input)
            lines_to_parse: list = self.input.splitlines()[1:]
        else:
            lines_to_parse = self.input.splitlines()

        self.count = len(lines_to_parse)
        self._rows: list = []
        self._preprocessed_results: list = []
        for line in lines_to_parse:
            parsing_results: list | tuple | set | dict = self.row_parser(line)
            self._rows.append(parsing_results)

            if self.row_preprocessor:
                self._preprocessed_results.append(self.row_preprocessor(parsing_results))

    @property
    def rows(self, present_as_dict: bool = False) -> list[list | tuple | set | dict]:
        if present_as_dict:
            assert self.header, "Header must be present to present rows as dict."

        if not present_as_dict:
            yield from self._rows
        else:
            for row in self._rows:
                assert len(row) == len(self.header), f"Row length must be equal to header length to present rows as dict. {len(row) = } != {len(self.header) = } | {row = } | {self.header = }"
                yield dict(zip(self.header, row))

    @property
    def preprocessed_results(self) -> list:
        return self._preprocessed_results
