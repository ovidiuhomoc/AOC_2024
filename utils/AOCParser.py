class AOCParser:

    def __init__(self, input_str: str, row_parser: callable, has_header: bool = False, header_parser: callable or None = None):
        self.input = input_str
        self.has_header = has_header
        self.row_parser = row_parser
        self.header_parser = header_parser

        self.count: int = 0

        self.header: list | None = None
        self.rows: list | None = None

    def parse(self):
        if self.has_header:
            self.header = self.header_parser(self.input)
            lines_to_parse: list = self.input.splitlines()[1:]
        else:
            lines_to_parse = self.input.splitlines()

        self.count = len(lines_to_parse)
        self.rows: list = list(map(self.row_parser, lines_to_parse))
