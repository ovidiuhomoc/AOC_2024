import copy
from dataclasses import dataclass
from typing import Literal

import day09


@dataclass
class Chunk:
    chunk_type: Literal["data", "free_space"]
    length: int
    id: int | None = None


def main(input: str, part: int = 1):
    fixed_input = input if len(input) % 2 == 0 else input + '0'
    disk_map = []

    file_id = 0
    blocks = []

    for files_length_candidate, free_space_length_candidate in zip(fixed_input[0::2], fixed_input[1::2]):
        files_length = int(files_length_candidate)
        free_space_length = int(free_space_length_candidate)

        blocks = blocks + [file_id] * files_length + ['.'] * free_space_length
        disk_map.append(Chunk("data", files_length, file_id))
        disk_map.append(Chunk("free_space", free_space_length))
        file_id += 1

    if part == 1:
        moved_blocks = copy.deepcopy(blocks)

        first_pointer = 0
        last_pointer = len(moved_blocks) - 1

        while first_pointer < last_pointer:
            if moved_blocks[first_pointer] != '.':
                first_pointer += 1
                continue

            if moved_blocks[last_pointer] == '.':
                last_pointer -= 1
                continue

            moved_blocks[first_pointer], moved_blocks[last_pointer] = moved_blocks[last_pointer], moved_blocks[first_pointer]

        sum = 0
        for pos, item in enumerate(moved_blocks):
            if item != '.':
                sum += pos * item

        return sum
    else:
        modif_disk_map = copy.deepcopy(disk_map)
        modif_disk_map = compact_disk(modif_disk_map)

        moved_blocks = []
        for chunk in modif_disk_map:
            if chunk.chunk_type == "data":
                moved_blocks += [chunk.id] * chunk.length
            else:
                moved_blocks += ['.'] * chunk.length

        sum = 0
        for pos, item in enumerate(moved_blocks):
            if item != '.':
                sum += pos * item

        return sum


def compact_disk(modif_disk_map):
    solved_list = [modif_disk_map[0].id]
    while True:
        chunk_to_move = None
        chunk_index = None

        for c_index in range(len(modif_disk_map))[::-1]:
            if modif_disk_map[c_index].chunk_type == "data" and modif_disk_map[c_index].id not in solved_list:
                chunk_to_move = modif_disk_map[c_index]
                chunk_index = c_index
                break

        if chunk_to_move is None:
            break

        # find a free spot big enough to move the chunk
        free_space_index = None
        free_space_length = None

        for c_index in range(chunk_index):
            if modif_disk_map[c_index].chunk_type == "free_space" and modif_disk_map[c_index].length >= chunk_to_move.length:
                free_space_index = c_index
                free_space_length = modif_disk_map[c_index].length
                break

        if free_space_index is None:
            solved_list.append(chunk_to_move.id)
            continue

        # move the chunk
        if free_space_length == chunk_to_move.length:
            # the space is exactly the same size as the chunk
            modif_disk_map[free_space_index], modif_disk_map[chunk_index] = modif_disk_map[chunk_index], modif_disk_map[free_space_index]
            solved_list.append(chunk_to_move.id)
            filter_disk_map(modif_disk_map)
            continue
        else:
            # the space is bigger than the chunk
            disk_map_until_free_space = modif_disk_map[:free_space_index]
            disk_map_between_free_space_and_chunk = modif_disk_map[free_space_index + 1:chunk_index]
            disk_map_after_chunk = modif_disk_map[chunk_index + 1:]

            leftover_space = Chunk("free_space", free_space_length - chunk_to_move.length)
            free_space_replacing_chunk = Chunk("free_space", chunk_to_move.length)

            modif_disk_map[:] = disk_map_until_free_space + [chunk_to_move] + [leftover_space] + disk_map_between_free_space_and_chunk + [free_space_replacing_chunk] + disk_map_after_chunk

            solved_list.append(chunk_to_move.id)
            filter_disk_map(modif_disk_map)
            continue

    return modif_disk_map


def filter_disk_map(modif_disk_map):
    modif_disk_map[:] = [chunk for chunk in modif_disk_map if chunk.chunk_type == "data" or (chunk.chunk_type == "free_space" and chunk.length > 0)]

    all_spaces_united = False
    while not all_spaces_united:
        all_spaces_united = True
        for c_index in range(len(modif_disk_map))[::-1]:
            if modif_disk_map[c_index].chunk_type == "free_space" and c_index + 1 < len(modif_disk_map) and modif_disk_map[c_index + 1].chunk_type == "free_space":
                modif_disk_map[c_index + 1].length += modif_disk_map[c_index].length
                modif_disk_map.pop(c_index)
                all_spaces_united = False
                break


if __name__ == '__main__':
    dinput = day09.demoinput
    input = day09.input1

    # print(f"{main(dinput, part=1) = }")
    # print(f"{main(input, part=1) = }")
    # print(f"{main(dinput, part=2) = }")
    print(f"{main(input, part=2) = }")
