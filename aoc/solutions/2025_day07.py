from aoc.solutions.base import BaseSolution


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2025, day=7)

    def solve(self):
        content = self.get_input_data()

        sol_1 = self.solve_part_1(content)
        sol_2 = self.solve_part_2(content)

        print(f"Solution for 2025 Day 7 Part 1: {sol_1}")
        print(f"Solution for 2025 Day 7 Part 2: {sol_2}")

    def solve_part_1(self, content: str) -> int:
        lines = content.splitlines()

        total_split = 0
        current_beam_idx = [lines[0].index("S")]
        for line in lines[1:]:
            only_dot = all(c == "." for c in line)
            if only_dot:
                continue
            new_beam_idx = []
            for idx in current_beam_idx:
                if line[idx] == "^":
                    total_split += 1
                    new_beam_idx.extend([idx - 1, idx + 1])
                else:
                    new_beam_idx.append(idx)
            current_beam_idx = list(set(new_beam_idx))
        return total_split

    def solve_part_2(self, content: str) -> int:
        lines = content.splitlines()

        current_beam_idx = {lines[0].index("S"): 1}
        for line in lines[1:]:
            only_dot = all(c == "." for c in line)
            if only_dot:
                continue
            new_beam_idx = {}
            for idx in current_beam_idx:
                if line[idx] == "^":
                    new_beam_idx[idx - 1] = current_beam_idx[idx] + new_beam_idx.get(
                        idx - 1, 0
                    )
                    new_beam_idx[idx + 1] = current_beam_idx[idx] + new_beam_idx.get(
                        idx + 1, 0
                    )
                else:
                    new_beam_idx[idx] = current_beam_idx[idx] + new_beam_idx.get(idx, 0)
            current_beam_idx = new_beam_idx.copy()

        total_timeline = sum(current_beam_idx.values())

        return total_timeline


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
