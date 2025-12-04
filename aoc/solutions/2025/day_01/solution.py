from pathlib import Path

from aoc.utils.get_data import get_local_data_txt


def solve():
    current_dir = Path(__file__).parent

    content = get_local_data_txt(current_dir)
    rotation_list = content.splitlines()

    sol_1 = solve_part_1(rotation_list)
    sol_2 = solve_part_2(rotation_list)

    print(f"Answer for Part 1: {sol_1}")
    print(f"Answer for Part 2: {sol_2}")


def solve_part_1(rotation_list: list[str]) -> int:
    position = 50
    num_zero = 0
    for rot in rotation_list:
        if rot[0] == "L":
            position -= int(rot[1:])
        elif rot[0] == "R":
            position += int(rot[1:])
        else:
            raise ValueError(f"Unknown rotation: {rot}")
        if position % 100 == 0:
            num_zero += 1
    return num_zero


def solve_part_2(rotation_list: list[str]) -> int:
    position = 50
    num_zero_click = 0
    for rot in rotation_list:
        if rot[0] == "L":
            step = -int(rot[1:])
        elif rot[0] == "R":
            step = int(rot[1:])
        else:
            raise ValueError(f"Unknown rotation: {rot}")
        if step >= 0:
            num_zero_click += (position + step) // 100 - position // 100
        else:
            # minus 1 to exclude the cases when old position is at 0 or new position is at 0
            # e.g., position = 0, new_position = 199, the count should be 0
            # e.g., position = 201, new_position = 100, the count should be 2
            num_zero_click += (position - 1) // 100 - (position + step - 1) // 100
        position = position + step
    return num_zero_click


if __name__ == "__main__":
    solve()
