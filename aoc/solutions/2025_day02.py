from aoc.solutions.base import BaseSolution
from aoc.utils.math_utils import find_factors


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2025, day=2)

    def solve(self):
        content = self.get_input_data()
        range_list = content.split(",")

        sol_1 = self.solve_part_1(range_list)
        sol_2 = self.solve_part_2(range_list)

        print(f"Answer for Part 1: {sol_1}")
        print(f"Answer for Part 2: {sol_2}")

    def solve_part_1(self, range_list: list[str]) -> int:
        sum = 0
        for r in range_list:
            left, right = r.split("-")[0], r.split("-")[1]
            if len(left) == len(right) and len(left) % 2 != 0:
                continue
            elif len(left) == len(right) and len(left) % 2 == 0:
                if int(left[: len(left) // 2]) >= int(left[len(right) // 2 :]):
                    start = int(left[: len(left) // 2])
                else:
                    start = int(left[: len(left) // 2]) + 1
                if int(right[: len(right) // 2]) <= int(right[len(right) // 2 :]):
                    end = int(right[: len(right) // 2])
                else:
                    end = int(right[: len(right) // 2]) - 1
                sum += (
                    (start + end)
                    * (end - start + 1)
                    // 2
                    * (10 ** (len(left) // 2) + 1)
                )
            else:
                subrange_list = []
                while len(left) < len(right):
                    subrange_list.append(f"{left}-{'9' * len(left)}")
                    left = "1" + "0" * len(left)
                subrange_list.append(f"{left}-{right}")
                sum += self.solve_part_1(subrange_list)
        return sum

    def solve_part_2(self, range_list: list[str]) -> int:
        sum = 0
        for r in range_list:
            left, right = r.split("-")[0], r.split("-")[1]
            left_factors = find_factors(len(left))
            left_factors = set(left_factors)
            for i in left_factors.copy():
                left_factors -= set(find_factors(i))
            left_factors = sorted(left_factors)
            delta_sum = 0
            if len(left) == len(right) and len(left) == 1:
                continue
            elif len(left) == len(right) and len(left_factors) == 0:
                delta_sum += self.calculate_sum_of_repdigit(left, right)
            elif len(left) == len(right) and len(left_factors) > 0:
                for f in left_factors:
                    start = int(left[:f])
                    end = int(right[:f])
                    if int(left[f:]) > start * int(
                        ("0" * (f - 1) + "1") * (len(left) // f - 1)
                    ):
                        start += 1
                    if int(right[f:]) < end * int(
                        ("0" * (f - 1) + "1") * (len(left) // f - 1)
                    ):
                        end -= 1
                    base = int(("0" * (f - 1) + "1") * (len(left) // f))
                    delta_sum += (start + end) * (end - start + 1) // 2 * base
                delta_sum -= self.calculate_sum_of_repdigit(left, right) * (
                    len(left_factors) - 1
                )
            else:
                subrange_list = []
                while len(left) < len(right):
                    subrange_list.append(f"{left}-{'9' * len(left)}")
                    left = "1" + "0" * len(left)
                subrange_list.append(f"{left}-{right}")
                delta_sum += self.solve_part_2(subrange_list)

            print(f"{r}\t{delta_sum}")
            sum += delta_sum

        return sum

    def calculate_sum_of_repdigit(self, left: str, right: str) -> int:
        assert len(left) == len(right), "Left and right must have the same length"
        start = int(left)
        end = int(right)
        repdigit_multiplier = int("1" * len(left))
        sum = 0
        for i in range(1, 10):
            rd = i * repdigit_multiplier
            if start <= rd <= end:
                sum += rd
        return sum


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
