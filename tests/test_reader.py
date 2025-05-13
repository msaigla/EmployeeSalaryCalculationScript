from pathlib import Path
from typing import List, Dict, Union
from src.utils.reader import read_employees

Employee = Dict[str, Union[str, int]]

def test_read_employees(sample_csv: Path) -> None:
    result: List[Employee] = read_employees(str(sample_csv))
    assert len(result) == 3
    assert result[0]['name'] == 'Alice'
    assert result[1]['rate'] == 40