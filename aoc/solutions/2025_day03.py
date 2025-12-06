from aoc.solutions.base import BaseSolution


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2025, day=3)

    def solve(self):
        content = self.get_input_data()
        lines = content.splitlines()

        sol_1 = self.solve_part_1(lines)
        sol_2 = self.solve_part_2(lines)

        print(f"Answer for Part 1: {sol_1}")
        print(f"Answer for Part 2: {sol_2}")

    def solve_part_1(self, lines: list[str]) -> int:
        sum = 0
        for line in lines:
            num_list = [int(c) for c in line]

            tens = num_list[0]
            ones = num_list[1]
            for i in range(1, len(num_list)):
                if num_list[i] > tens and i != len(num_list) - 1:
                    tens = num_list[i]
                    ones = num_list[i + 1]
                elif num_list[i] > ones:
                    ones = num_list[i]
            # print(f"{line}\t{tens * 10 + ones}")
            sum += tens * 10 + ones
        return sum

    def solve_part_2(self, lines: list[str]) -> int:
        sum = 0
        for line in lines:
            assert len(line) >= 12
            num_list = [int(c) for c in line]
            digits_idx = list(range(12))
            for i in range(1, len(num_list)):
                for j in range(12):
                    if digits_idx[j] >= i:
                        break
                    if num_list[i] > num_list[digits_idx[j]] and i + (12 - j) <= len(
                        num_list
                    ):
                        digits_idx[j] = i
                        for k in range(j + 1, 12):
                            digits_idx[k] = i + (k - j)
                        break
            digits = [num_list[idx] for idx in digits_idx]
            # print(f"{line}\t{''.join([str(d) for d in digits])}")
            sum += int("".join([str(d) for d in digits]))
        return sum


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
