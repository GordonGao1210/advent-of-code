import numpy as np

from aoc.solutions.base import BaseSolution


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2025, day=4)

    def solve(self):
        content = self.get_input_data()

        sol_1, _ = self.solve_part_1(content)
        sol_2 = self.solve_part_2(content)

        print(f"Solution for 2025 Day 4 Part 1: {sol_1}")
        print(f"Solution for 2025 Day 4 Part 2: {sol_2}")

    def solve_part_1(self, content: str | np.ndarray) -> tuple[int, np.ndarray]:
        matrix = self.convert_content_to_matrix(content)
        matrix_ext = np.pad(matrix, pad_width=1, mode="constant", constant_values=0)
        sum_result = np.zeros(matrix.shape, dtype=int)
        for i in range(0, 3):
            for j in range(0, 3):
                sub_matrix = matrix_ext[
                    i : i + matrix.shape[0], j : j + matrix.shape[1]
                ]
                sum_result += sub_matrix
        sum_result = sum_result - matrix
        count = ((sum_result < 4) & (matrix == 1)).sum()
        matrix[(sum_result < 4) & (matrix == 1)] = 0
        return count, matrix

    def convert_content_to_matrix(self, content: str | np.ndarray) -> np.ndarray:
        if isinstance(content, np.ndarray):
            return content
        elif isinstance(content, str):
            matrix = []
            for line in content.splitlines():
                row = []
                for i in range(len(line)):
                    row.append(1 if line[i] == "@" else 0)
                matrix.append(row)
            return np.array(matrix)
        else:
            raise ValueError("Unsupported content type for conversion to matrix.")

    def solve_part_2(self, content: str) -> int:
        matrix = self.convert_content_to_matrix(content)
        count = 0
        while True:
            c, matrix = self.solve_part_1(matrix)
            if c == 0:
                break
            count += c
        return count


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
