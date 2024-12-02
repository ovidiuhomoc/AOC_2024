from utils.AOCParser import AOCParser


def row_parser(row: str) -> list[int]:
    return list(map(int, str(row).split()))


def row_preprocessor(row: list[int]) -> int:
    return sum(row)


if __name__ == '__main__':
    aocp = AOCParser(input_str="""1 2 3
    4 5 6""",
                     row_parser=row_parser,
                     has_header=False,
                     header_parser=None,
                     row_preprocessor=row_preprocessor)

    aocp.parse()

    for index, row in enumerate(aocp.rows):
        print(f"Row {index}: {row}")
        print(f"Preprocessed Row {index}: {aocp.preprocessed_results[index]}")
        print()
