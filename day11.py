from functools import lru_cache

import day11


@lru_cache(maxsize=5 * 1024)
def process_stone(stone: int) -> tuple | int:
    # rule 1
    if stone == 0:
        return 1

    # rule 2
    str_repr = str(stone)
    if len(str_repr) % 2 == 0:
        # return the first and second halfs of the string as integers
        half_pos = len(str_repr) // 2
        return int(str_repr[:half_pos]), int(str_repr[half_pos:])

    # rule 3
    return stone * 2024


@lru_cache(maxsize=5 * 1024)
def get_stone_number_over_blinks(stone: int, max_blinks: int, current_blink: int) -> int:
    if current_blink == max_blinks:
        return 1

    current_blink_stones: list[int] = []
    resulted_stones: tuple | int = process_stone(stone)

    if isinstance(resulted_stones, tuple):
        current_blink_stones = [resulted_stone for resulted_stone in resulted_stones]
    else:
        current_blink_stones = [resulted_stones]

    # print(f"At blink {current_blink}, the input was {stone} and stones output is: {current_blink_stones}")

    stone_count = 0
    for stone in current_blink_stones:
        results_count = get_stone_number_over_blinks(stone, max_blinks, current_blink + 1)
        stone_count += results_count

    return stone_count


def main(input: str, part: int = 1):
    initial_stones = list(map(int, input.split()))

    # stones = copy.deepcopy(initial_stones)

    blinks = 25 if part == 1 else 75

    # for blink in range(blinks):
    #     current_blink_stones: list[int] = []
    #
    #     for stone in stones:
    #         resulted_stones: tuple | int = process_stone(stone)
    #
    #         if isinstance(resulted_stones, tuple):
    #             current_blink_stones = current_blink_stones + list(resulted_stones)
    #         else:
    #             current_blink_stones.append(resulted_stones)
    #
    #     print(f"At blink {blink + 1}, stones are: {current_blink_stones}")
    #     print()
    #     stones = current_blink_stones

    sum = 0
    for stone in initial_stones:
        sum += get_stone_number_over_blinks(stone=stone, max_blinks=blinks, current_blink=0)

    return sum


if __name__ == '__main__':
    dinput = day11.demoinput
    dinput2 = day11.demoinput2
    input1 = day11.input1

    # print(f"{main(dinput, part=1) = }")
    # print(f"{main(dinput2, part=1) = }")
    # print(f"{main(input1, part=1) = }")
    print(f"{main(input1, part=2) = }")
