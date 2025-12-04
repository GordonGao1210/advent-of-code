from pathlib import Path


def get_local_data_txt(solution_dir: Path) -> str:
    year = solution_dir.parent.name
    day = solution_dir.name

    input_path = solution_dir.parent.parent.parent / "data" / year / day / "input.txt"

    with open(input_path, "r") as f:
        content = f.read()

    return content
