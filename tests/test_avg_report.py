from pathlib import Path
from typing import List, Dict, Union

from src.utils.reader import read_employees
from src.reports.avg_report import AvgReport

Employee = Dict[str, Union[str, int]]

def test_avg_report_output(sample_csv: Path) -> None:
    employees: List[Employee] = read_employees(str(sample_csv))
    report: str = AvgReport(employees).generate()

    assert "Design" in report
    assert "avg: 50" in report  # (40 + 60) / 2
    assert "Marketing" in report
    assert "avg: 50" in report  # only one employee
