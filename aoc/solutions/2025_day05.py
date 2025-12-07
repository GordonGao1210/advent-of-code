from aoc.solutions.base import BaseSolution


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2025, day=5)

    def solve(self):
        content = self.get_input_data()

        sol_1 = self.solve_part_1(content)
        sol_2 = self.solve_part_2(content)

        print(f"Solution for 2025 Day 5 Part 1: {sol_1}")
        print(f"Solution for 2025 Day 5 Part 2: {sol_2}")

    def solve_part_1(self, content: str) -> int:
        ranges, ids = content.split("\n\n")
        id_list = sorted([int(ele) for ele in ids.splitlines()])
        range_list = sorted(
            [
                (int(ele.split("-")[0]), int(ele.split("-")[1]))
                for ele in ranges.splitlines()
            ]
        )

        count = 0
        i = 0
        for id in id_list:
            while True:
                start, end = range_list[i]
                if id < start:
                    break
                elif start <= id <= end:
                    count += 1
                    break
                else:
                    i += 1
                    if i >= len(range_list):
                        return count
        return count

    def solve_part_2(self, content: str) -> int:
        ranges, _ = content.split("\n\n")
        range_list = sorted(
            [
                (int(ele.split("-")[0]), int(ele.split("-")[1]))
                for ele in ranges.splitlines()
            ]
        )

        merged_ranges = []
        for start, end in range_list:
            if not merged_ranges:
                merged_ranges.append((start, end))
            else:
                last_start, last_end = merged_ranges[-1]
                if start <= last_end:
                    merged_ranges[-1] = (last_start, max(last_end, end))
                else:
                    merged_ranges.append((start, end))

        count = 0
        for start, end in merged_ranges:
            print(f"{start}-{end}")
            count += end - start + 1
        return count


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
