from math import prod

from aoc.solutions.base import BaseSolution
from aoc.utils.math_utils import calculate_euclidean_distance


class Solution(BaseSolution):
    def __init__(self):
        super().__init__(year=2025, day=8)

    def solve(self):
        content = self.get_input_data()

        sol_1 = self.solve_part_1(content)
        sol_2 = self.solve_part_2(content)

        print(f"Solution for 2025 Day 8 Part 1: {sol_1}")
        print(f"Solution for 2025 Day 8 Part 2: {sol_2}")

    def solve_part_1(self, content: str) -> int:
        lines = content.splitlines()
        boxes = [list(map(int, line.split(","))) for line in lines]

        distance = {}
        for i in range(len(lines)):
            for j in range(i + 1, len(lines)):
                distance[(i, j)] = calculate_euclidean_distance(boxes[i], boxes[j])

        sorted_pairs = sorted(distance, key=lambda k: distance[k])
        circuits: list[set] = []
        connected_box = set()
        for i in range(1000):
            box_1_idx, box_2_idx = sorted_pairs[i]
            if box_1_idx not in connected_box and box_2_idx not in connected_box:
                circuits.append({box_1_idx, box_2_idx})
            else:
                box_1_exists_in = None
                box_2_exists_in = None
                for j in range(len(circuits)):
                    if box_1_idx in circuits[j]:
                        box_1_exists_in = j
                    if box_2_idx in circuits[j]:
                        box_2_exists_in = j
                if box_1_exists_in is not None and box_2_exists_in is not None:
                    if box_1_exists_in != box_2_exists_in:
                        set_1, set_2 = [
                            circuits.pop(k)
                            for k in sorted(
                                [box_1_exists_in, box_2_exists_in], reverse=True
                            )
                        ]
                        circuits.append(set_1.union(set_2))
                elif box_1_exists_in is not None:
                    circuits[box_1_exists_in].add(box_2_idx)
                elif box_2_exists_in is not None:
                    circuits[box_2_exists_in].add(box_1_idx)
                else:
                    raise ValueError
            connected_box.update({box_1_idx, box_2_idx})
        sorted_circuits = sorted(circuits, key=lambda c: len(c), reverse=True)

        product = prod([len(sorted_circuits[i]) for i in range(3)])

        return product

    def solve_part_2(self, content: str) -> int:
        lines = content.splitlines()
        boxes = [list(map(int, line.split(","))) for line in lines]

        distance = {}
        for i in range(len(lines)):
            for j in range(i + 1, len(lines)):
                distance[(i, j)] = calculate_euclidean_distance(boxes[i], boxes[j])

        sorted_pairs = sorted(distance, key=lambda k: distance[k])
        roots = list(range(len(boxes)))

        def find_root(box_idx: int) -> int:
            # only when the root of the box is itself, we have found the root
            while roots[box_idx] != box_idx:
                # update root on the fly for other boxes
                roots[box_idx] = roots[roots[box_idx]]
                box_idx = roots[box_idx]
            return roots[box_idx]

        n_left = len(boxes) - 1
        for i in range(len(sorted_pairs)):
            box_1_idx, box_2_idx = sorted_pairs[i]
            root_1 = find_root(box_1_idx)
            root_2 = find_root(box_2_idx)
            if root_1 != root_2:
                roots[root_2] = root_1
                n_left -= 1
            if n_left == 0:
                break
        last_pair = sorted_pairs[i]
        box_1_idx, box_2_idx = last_pair
        return boxes[box_1_idx][0] * boxes[box_2_idx][0]


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
