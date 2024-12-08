from functools import cache

import day07


@cache
def evaluate_equation(operands: tuple[int], operators: tuple[str]) -> int:
    result = operands[0]
    for i in range(1, len(operands)):
        if operators[i - 1] == "+":
            result += operands[i]
        elif operators[i - 1] == "*":
            result *= operands[i]
        elif operators[i - 1] == "||":
            result = int(f"{result}{operands[i]}")
        else:
            raise ValueError(f"Unknown operator: {operators[i - 1]}")

    return result


def get_recursive_results(operands: tuple[int, ...], operand_index: int, operators: list[str], part: int = 1, expected_result: int | None = None) -> list[int]:
    assert part in [1, 2], f"Invalid part: {part}"

    if operand_index == len(operands) - 1:
        return [evaluate_equation(operands, tuple(operators))]

    # it is not yet the last operand. Evaluate equation so far and exit if it is already greater than expected result
    if expected_result is not None and operand_index > 0:  # at least 1 operator and 2 operands
        result_so_far = evaluate_equation(operands[:operand_index], tuple(operators))
        if result_so_far > expected_result:
            return []

    if part == 1:
        return get_recursive_results(operands, operand_index + 1, operators + ["+"]) + get_recursive_results(operands, operand_index + 1, operators + ["*"])
    elif part == 2:
        return get_recursive_results(operands, operand_index + 1, operators + ["+"], part=2, expected_result=expected_result) + get_recursive_results(operands, operand_index + 1, operators + ["*"], part=2, expected_result=expected_result) + get_recursive_results(operands, operand_index + 1, operators + ["||"], part=2, expected_result=expected_result)


def process(input: str, part: int = 1):
    equations = []

    results_sum = 0

    for line in input.splitlines():
        expected_result: int = int(line.split(":")[0])
        operands: list[int] = list(map(int, line.split(":")[1].strip().split(" ")))
        equations.append((expected_result, tuple(operands)))

        computed_results: list[int] = get_recursive_results(operands=tuple(operands), operand_index=0, operators=[]) if part == 1 else get_recursive_results(operands=tuple(operands), operand_index=0, operators=[], part=2, expected_result=expected_result)
        if expected_result in computed_results:
            results_sum += expected_result

    return results_sum


if __name__ == '__main__':
    input = day07.demoinput
    # input = day07.input1

    print(f"{process(input, part=1) = }")
    print(f"{process(input, part=2) = }")
