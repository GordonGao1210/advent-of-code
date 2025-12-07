import math

from aoc.solutions.base import BaseSolution


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2025, day=6)

    def solve(self):
        content = self.get_input_data()

        sol_1 = self.solve_part_1(content)
        sol_2 = self.solve_part_2(content)

        print(f"Solution for 2025 Day 6 Part 1: {sol_1}")
        print(f"Solution for 2025 Day 6 Part 2: {sol_2}")

    def solve_part_1(self, content: str) -> int:
        lines = content.splitlines()
        rows = []
        for line in lines[:-1]:
            row = [int(ele) for ele in line.split()]
            rows.append(row)
        rows.append(lines[-1].split())

        total = 0
        for i in range(len(rows[0])):
            if rows[-1][i] == "*":
                total += math.prod([rows[j][i] for j in range(len(rows) - 1)])
            elif rows[-1][i] == "+":
                total += sum([rows[j][i] for j in range(len(rows) - 1)])
            else:
                raise ValueError("Unknown operation")
        return total

    def solve_part_2(self, content: str) -> int:
        rows = content.splitlines()
        groups = self.split_by_vertical_space(rows)

        total = 0
        for group in groups:
            operation = group[-1].strip()
            numbers = []
            for i in range(len(group[0])):
                num_str = "".join([group[j][i] for j in range(len(group) - 1)]).strip()
                numbers.append(int(num_str))
            if operation == "*":
                total += math.prod(numbers)
            elif operation == "+":
                total += sum(numbers)
            else:
                raise ValueError("Unknown operation")
        return total

    def split_by_vertical_space(self, rows: list[str]) -> list[list[str]]:
        groups = []
        for i in range(len(rows)):
            rows[i] = " " + rows[i]

        i = len(rows[0]) - 1
        last_i = len(rows[0]) - 1
        while i >= 0:
            check_space = [rows[j][i] == " " for j in range(len(rows))]
            if all(check_space):
                group = []
                for row in rows:
                    group.append(row[i + 1 : last_i + 1])
                groups.append(group)
                last_i = i - 1
                i -= 1
            else:
                i -= 1

        return groups


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
