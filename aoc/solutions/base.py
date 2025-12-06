import os
from abc import ABC, abstractmethod


class BaseSolution(ABC):
    def __init__(self, year: int, day: int):
        self.year = year
        self.day = day

    @abstractmethod
    def solve(self):
        pass

    def get_input_data(self) -> str:
        year = str(self.year)
        day = f"{self.day:02d}"
        input_path = os.path.join("aoc", "data", f"{year}_day{day}.txt")
        with open(input_path, "r") as f:
            content = f.read()
        return content
