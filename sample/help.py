from typing import List, Any


def create_grid_by_str(string: str):
    result: List[List[int]] = [
        [
            int(s) for s in line if not s.isspace()
        ] for line in string.splitlines() if line
    ]
    return result
