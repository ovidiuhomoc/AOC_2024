import re

import day03

mul_pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')


def part1(string: str):
    total_sum = 0
    matches = mul_pattern.findall(string)
    for match in matches:
        total_sum += int(match[0]) * int(match[1])

    return total_sum


def part2_optimized(string: str):
    valid_window_pattern = r'do\(\)(.*?)don\'t\(\)'

    match = re.findall(valid_window_pattern, "do()" + string + "don't()", re.DOTALL)
    assert match, "No valid window found"

    total_mul_sum = 0
    for window in match:
        section_mul_sum = part1(window)
        total_mul_sum += section_mul_sum

    return total_mul_sum


def part2(string: str):
    total_mul_sum = 0

    muls = []
    dos_and_donts = []

    complete_string = str(string).lower()
    window_size = 12

    for ch_index in range(len(string)):
        string_to_check = complete_string[ch_index:ch_index + window_size]
        match = mul_pattern.match(string_to_check)

        if match and string_to_check.startswith('mul('):
            muls.append((ch_index, (int(match[1]), int(match[2]))))

        if string_to_check.startswith('do()'):
            dos_and_donts.append((ch_index, 'do'))

        if string_to_check.startswith("don't()"):
            dos_and_donts.append((ch_index, 'dont'))

    section_type = 'do'
    for i in range(len(string)):
        this_is_a_mull = False

        a = None
        b = None

        for start, type in dos_and_donts:
            if start == i:
                section_type = type
                if section_type == "do":
                    print(f"pos {start} - do section")
                else:
                    print(f"pos {start} - don't section")
                break

        for start, mul in muls:
            if start == i:
                this_is_a_mull = True
                a, b = mul
                break

        if this_is_a_mull:
            if section_type == 'do':
                total_mul_sum += a * b

    return total_mul_sum


if __name__ == '__main__':
    print(f"{part1(day03.demoinput) = }")
    print()

    print(f"{part2(day03.demoinput2) = }")
    print()
    print(f"{part2(day03.input1) = }")
    print()

    print(f"{part2_optimized(day03.demoinput2) = }")
    print(f"{part2_optimized(day03.input1) = }")
