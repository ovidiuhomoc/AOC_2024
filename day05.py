from functools import cache

import day05

post_presence_rules = {}


def is_valid_update(update: list[int]) -> bool:
    for page_pos, page in enumerate(update[:-1]):
        for second_page in update[page_pos + 1:]:
            if post_presence_rules.get(second_page) and page in post_presence_rules[second_page]:
                return False
    return True


@cache
def cached_is_valid_update(update: tuple[int]) -> tuple[bool, int | None, int | None]:
    for page_pos, page in enumerate(update[:-1]):
        second_page_pos = page_pos + 1
        while second_page_pos < len(update):
            second_page = update[second_page_pos]
            if post_presence_rules.get(second_page) and page in post_presence_rules[second_page]:
                return False, page_pos, second_page_pos
            second_page_pos += 1
    return True, None, None


def fix_update(update: list[int]) -> list[int]:
    fix_applied = True
    local_update = update.copy()

    while fix_applied:
        fix_applied = False

        for page_pos, page in enumerate(local_update):
            success, to_repl_page_pos, to_repl_second_page_pos = cached_is_valid_update(tuple(local_update[:page_pos + 1]))
            while not success:
                fix_applied = True
                # swap the two pages
                local_update[to_repl_page_pos], local_update[to_repl_second_page_pos] = local_update[to_repl_second_page_pos], local_update[to_repl_page_pos]
                success, to_repl_page_pos, to_repl_second_page_pos = cached_is_valid_update(tuple(local_update[:page_pos + 1]))

    return local_update


def part1(input: str):
    rules_str = input.split("\n\n")[0]
    updates_str = input.split("\n\n")[1]

    for rule in rules_str.splitlines():
        rule_int_tuple = tuple(map(int, rule.split("|")))
        post_presence_rules.setdefault(rule_int_tuple[0], []).append(rule_int_tuple[1])

    updates = []
    for update in updates_str.splitlines():
        updates.append(list(map(int, update.split(','))))

    sum = 0
    for update in updates:
        if is_valid_update(update):
            # check if it is an odd length
            assert len(update) % 2 != 0, f"Update length is even. {update = }"

            # add top sum the middle element
            sum += update[len(update) // 2]

    return sum


def part2(input: str):
    rules_str = input.split("\n\n")[0]
    updates_str = input.split("\n\n")[1]

    for rule in rules_str.splitlines():
        rule_int_tuple = tuple(map(int, rule.split("|")))
        post_presence_rules.setdefault(rule_int_tuple[0], []).append(rule_int_tuple[1])

    updates = []
    for update in updates_str.splitlines():
        updates.append(list(map(int, update.split(','))))

    sum = 0
    for update in updates:
        if is_valid_update(update):
            continue
        else:
            update = fix_update(update)
            sum += update[len(update) // 2]

    return sum


if __name__ == '__main__':
    # input = day05.demoinput
    input = day05.input1

    # part = part1
    part = part2

    print(f"{part(input) = }")
