class AOCParser:

    def __init__(self, input_str: str, row_parser: callable, has_header: bool = False, header_parser: callable or None = None):
        self.input = input_str
        self.has_header = has_header
        self.row_parser = row_parser
        self.header_parser = header_parser

        self.count: int = 0

        self.header: list | None = None
        self._rows: list | None = None

    def parse(self):
        if self.has_header:
            self.header = self.header_parser(self.input)
            lines_to_parse: list = self.input.splitlines()[1:]
        else:
            lines_to_parse = self.input.splitlines()

        self.count = len(lines_to_parse)
        self._rows: list = list(map(self.row_parser, lines_to_parse))

    @property
    def rows(self, present_as_dict: bool = False) -> list[list] | list[dict]:
        if present_as_dict:
            assert self.header, "Header must be present to present rows as dict."

        if not present_as_dict:
            yield from self._rows
        else:
            for row in self._rows:
                assert len(row) == len(self.header), f"Row length must be equal to header length to present rows as dict. {len(row) = } != {len(self.header) = } | {row = } | {self.header = }"
                yield dict(zip(self.header, row))
